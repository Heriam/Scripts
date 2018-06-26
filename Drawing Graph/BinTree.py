import xml.etree.ElementTree as ET
import xml.dom.minidom as paser
import multiprocessing
import json
import sys
sys.setrecursionlimit(100000)
import timeit as it
import numpy as np
import matplotlib.pyplot as plt

NUMS = range(200,2001,200)
REPEAT = 2000
NUMBER = 1

SJ = "scaledJSONPolicy.json"
DJ = "deepJSONPolicy.json"
SX = "scaledXACMLPolicy.xml"
DX = "deepXACMLPolicy.xml"
MEAN = 'mean'
VAR = 'var'

W = 'write'
L = 'load'
P = 'process'
M = 'memory'

NAMES = {
    'SJ': SJ,
    'DJ': DJ,
    'SX': SX,
    'DX': DX
}

POLICIES =  {}
for i in NUMS:
    POLICIES[str(i)] = {
    SJ: None,
    DJ: None,
    SX: None,
    DX: None
    }

BUILTPOLICIES = {}
for i in NUMS:
    BUILTPOLICIES[str(i)] = {
    SJ: None,
    DJ: None,
    SX: None,
    DX: None
    }

MSG = {"Subject": "Sam"}

# ========================================= Build Policies =========================================
def createXACMLPolicy(id=0):
    policyset = ET.Element("PolicySet")
    policyset.set('Version', '1')
    policyset.set('Id', str(id))
    policyset.set('Update', '2017-03-14 17:18:31')
    policyset.set('PolicyCombiningAlgorithm', 'allowOverrides')

    target = ET.SubElement(policyset, 'Target')
    subjects = ET.SubElement(target, 'Subjects')
    subject = ET.SubElement(subjects, 'Subject')

    subjectmatch = ET.SubElement(subject, 'SubjectMatch', MatchId="string-equal")
    ET.SubElement(subjectmatch, 'AttributeValue', DataType="string").text = "Sam"
    ET.SubElement(subjectmatch, 'SubjectAttributeDesignator', DataType="string", AttributeId="subject:subject-id")

    return policyset

def printXACMLPolicy(policy):
    print paser.parseString(ET.tostring(policy)).toprettyxml()

def buildXACMLScaledPolicy(num):
    policy = createXACMLPolicy()
    for i in range(num):
        policy.append(createXACMLPolicy(i+1))
    return ET.tostring(policy)

def buildXACMLDeepPolicy(num):
    policy = createXACMLPolicy()
    root = policy
    for i in range(num):
        root.append(createXACMLPolicy(i+1))
        root = root[1]
    return ET.tostring(policy)

def createJSONPolicy(id=0):
    return {
      "Id": id,
      "Version": 1,
      "Update": "2017-03-14 17:18:31",
      "Target": {"Subject": {"equals": "Sam"}},
      "PolicyCombiningAlgorithm": "allowOverrides",
      "Policies": []
    }

def printJSONPolicy(policy):
    print json.dumps(policy, indent=4)

def buildJSONScaledPolicy(num):
    policy = createJSONPolicy()
    for i in range(num):
        policy["Policies"].append(createJSONPolicy(i+1))
    return json.dumps(policy)

def buildJSONDeepPolicy(num):
    policy = createJSONPolicy()
    root = policy
    for i in range(num):
        root["Policies"].append(createJSONPolicy(i+1))
        root = root["Policies"][0]
    return json.dumps(policy)

FILES = {
    SJ: (buildJSONScaledPolicy, json.load),
    DJ: (buildJSONDeepPolicy, json.load),
    SX: (buildXACMLScaledPolicy, ET.parse),
    DX: (buildXACMLDeepPolicy, ET.parse)
}

def buildPolicies():
    for num in NUMS:
        for file, funcs in FILES.items():
            BUILTPOLICIES[str(num)][file] = funcs[0](num)

#========================================== W&R Policies ========================================

def writePolicy(num, file):
    with open('./{0}{1}'.format(num, file), 'w') as f:
        f.write(BUILTPOLICIES[str(num)][file])

def loadPolicy(num, file):
    with open('./{0}{1}'.format(num, file), 'r') as f:
        POLICIES[str(num)][file] = FILES[file][1](f)

#====================================== Process Policies ========================================

def verify(opt, a, b):
    if opt == "equals" or opt == "string-equal":
        return a == b
    else:
        raise Exception('unknown operation!')

def isJACPolApplicable(policy, msg=MSG):
    target = policy.get("Target")
    attribute, express = target.items()[0]
    operation, value = express.items()[0]
    if verify(operation, value, msg[attribute]):
        return True
    else:
        raise Exception('unexpected result!')

def isXACMLApplicable(policy, msg=MSG):
    target = policy[0]
    attrScaleEle = target[0]
    attributeEle = attrScaleEle[0]
    attriMatch = attributeEle[0]
    attributeVal = attriMatch[0]
    attribute = attributeEle.tag
    operation = attriMatch.get('MatchId')
    value = attributeVal.text
    if verify(operation, value, msg[attribute]):
        return True
    else:
        raise Exception('unexpected result!')

def processJSONPolicy(policy):
    stack = []
    if isJACPolApplicable(policy):
        stack.append(policy)
    while stack:
        policy = stack.pop()
        for child in policy["Policies"]:
            if isJACPolApplicable(child):
                stack.append(child)

def processXACMLPolicy(policy):
    stack = []
    policy = policy.getroot()
    if isXACMLApplicable(policy):
        stack.append(policy)
    while stack:
        policy = stack.pop()
        for child in policy.findall("PolicySet"):
            if isXACMLApplicable(child):
                stack.append(child)

def processPolicy(num, file):
    if 'JSON' in file:
        processJSONPolicy(POLICIES[str(num)][file])
    else:
        processXACMLPolicy(POLICIES[str(num)][file])

#=============================== Measure Metrics =================================

def measureRound(num):
    METRICS = {
        SJ: {W: {MEAN: None, VAR: None}, L: {MEAN: None, VAR: None}, P: {MEAN: None, VAR: None},
             M: {MEAN: None, VAR: None}},
        DJ: {W: {MEAN: None, VAR: None}, L: {MEAN: None, VAR: None}, P: {MEAN: None, VAR: None},
             M: {MEAN: None, VAR: None}},
        SX: {W: {MEAN: None, VAR: None}, L: {MEAN: None, VAR: None}, P: {MEAN: None, VAR: None},
             M: {MEAN: None, VAR: None}},
        DX: {W: {MEAN: None, VAR: None}, L: {MEAN: None, VAR: None}, P: {MEAN: None, VAR: None},
             M: {MEAN: None, VAR: None}},
    }
    for name, file in NAMES.items():
        w = it.repeat('writePolicy({0},{1})'.format(num, name), setup="from __main__ import writePolicy, {0}".format(name),
                      repeat=REPEAT, number=NUMBER)
        l = it.repeat('loadPolicy({0},{1})'.format(num, name), setup="from __main__ import loadPolicy, {0}".format(name),
                      repeat=REPEAT, number=NUMBER)
        p = it.repeat('processPolicy({0},{1})'.format(num, name), setup="from __main__ import processPolicy, {0}".format(name),
                      repeat=REPEAT, number=NUMBER)
        METRICS[file][W][MEAN] = np.mean(w)
        METRICS[file][W][VAR]  = np.var(w)
        METRICS[file][L][MEAN] = np.mean(l)
        METRICS[file][L][VAR]  = np.var(l)
        METRICS[file][P][MEAN] = np.mean(p)
        METRICS[file][P][VAR]  = np.var(p)
        METRICS[file][M][MEAN] = len(BUILTPOLICIES[str(num)][file].replace(" ", ""))
        METRICS[file][M][VAR]  = 0
        print num, name
    return (num, METRICS)

#=============================== Generate Graphics ================================

def plotWriteGraphics(results):
    for file in FILES.keys():
        x    = [r[0] for r in results]
        y    = [r[1][file][W][MEAN] for r in results]
        yerr = [r[1][file][W][VAR] for r in results]
        plt.figure()
        plt.errorbar(x, y)
        plt.show()

def multiprocess():
    buildPolicies()
    if __name__ == "__main__":
        pool = multiprocessing.Pool(processes=8)
        results = [pool.apply_async(measureRound, args=(num,)) for num in NUMS]
        results = [p.get() for p in results]
        results.sort()
        plotWriteGraphics(results)



multiprocess()





