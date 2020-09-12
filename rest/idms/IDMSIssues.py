#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, datetime
from requests_ntlm import HttpNtlmAuth
from Issue import Issue
import logging

# ----------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log.txt",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)
# ----------- Main Entry ------------------


class IDMSIssues:
    IDMS = 'http://idms.h3c.com'
    URL = 'http://idms.h3c.com/PersonalView/PersonalDefects?type=200'
    AUTH_URL = 'http://winauth.h3c.com/'
    RAW_DATA = 'sEcho=5&iColumns=14&sColumns=&iDisplayStart=0&iDisplayLength=1000&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&mDataProp_6=6&mDataProp_7=7&mDataProp_8=8&mDataProp_9=9&mDataProp_10=10&mDataProp_11=11&mDataProp_12=12&mDataProp_13=13&iSortCol_0=4&sSortDir_0=desc&iSortingCols=1&bSortable_0=false&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&bSortable_5=true&bSortable_6=true&bSortable_7=true&bSortable_8=true&bSortable_9=true&bSortable_10=true&bSortable_11=true&bSortable_12=true&bSortable_13=true&queryStr=%5B%7B+code%3A%22CurrentPerson%22%2CselectVal%3A%22%3D%22%2Cvalue%3A%22%26RD-AI-SA-Network%2Cxuezhetao+KF8948%2Cchelijun+02696%2C%22%2Cfiltertype%3A%22select%22%2Ctype%3A%22text%22+%7D%2C%7B+code%3A%22Status%22%2CselectVal%3A%22%3D%22%2Cvalue%3A%223%2C4%2C5%2C6%2CSuspend%2CA%2CB%2CC%22%2Cfiltertype%3A%22select%22+%7D%5D&total=29&orderColumns=SubmitDate+desc&displayColumns=DefectNO%2CSummery%2CStatus%2CCurrentPerson%2CPRODUCT%2CRELEASE%2CBASELINE%2CODC_Severity%2CLengthofstay%2CSubmitDate%2CSubmitBy%2CName_B%2CSyNo&customProfileId=bb3edf89-299e-419f-acd7-64a6b4b5c9f2'
    SEARCH_URL = 'http://idms.h3c.com/DefectSearch/Defects'
    SEARCH_RESOLVED_DATE_RAW = 'sEcho=1&iColumns=9&sColumns=&iDisplayStart=0&iDisplayLength=1000&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&mDataProp_6=6&mDataProp_7=7&mDataProp_8=8&iSortCol_0=1&sSortDir_0=desc&iSortingCols=1&bSortable_0=false&bSortable_1=true&bSortable_2=true&bSortable_3=true&bSortable_4=true&bSortable_5=true&bSortable_6=true&bSortable_7=true&bSortable_8=true&queryStr=%5B%7B+code%3A%22Status%22%2CselectVal%3A%22%3D%22%2Cvalue%3A%220%2CD%2CE%2CF%2CG%2CZ%22%2Cfiltertype%3A%22select%22+%7D%2C%7B+code%3A%22MemberCode1%22%2CselectVal%3A%22like%22%2Cvalue%3A%22%26RD-AI-SA-Network%2C+xuezhetao+KF8948%2C%22%2Cfiltertype%3A%22string%22+%7D%2C%7B+code%3A%22NodeCode%22%2CselectVal%3A%22like%22%2Cvalue%3A%22B%22%2Cfiltertype%3A%22string%22+%7D%2C%7B+code%3A%22DealMethod%22%2CselectVal%3A%22like%22%2Cvalue%3A%22070f28e8-553f-49ef-af38-7215d669922d%22%2Cfiltertype%3A%22string%22+%7D%2C%7B+code%3A%22DefectModifiedTime%22%2CselectVal%3A%22%22%2Cvalue%3A%22'+ '{{startDate}}' +'%2C' + '{{endDate}}' + '%22%2Cfiltertype%3A%22datetime%22+%7D%5D&type=Advanced'
    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate"
    }
    MEMBERS = {
        'jianghao 16492': [],
        'zhouhuan 20670': [],
        'zhangzhenwei 20674': [],
        'liuhuasheng YS1910': [],
        'zhaojun 22551': [],
        'chenyuanchun 21706': [],
        'lansongnian 22216': [],
        'huangsiming 20254': [],
        'lihongcheng 21166': [],
        'linyongxing 21167': [],
        'zhangzhile 20988': [],
        'xuezhetao KF8948': [],
        'liuzhe 20255': [],
    }
    idmsIssueList = []

    def __init__(self):
        self.s = requests.Session()
        self.s.auth = HttpNtlmAuth('h3c\\j16492', 'Jh203142')
        self.s.get(self.IDMS)
        r = json.loads(self.s.post(url=self.URL, headers=self.HEADERS, data=self.RAW_DATA).content.decode("utf-8"))
        for issue in (r['aaData']):
            currentStaff = issue[4]
            fixedBy = issue[12]
            description = issue[2].split('<label>')[1].strip('</label>').replace('&nbsp;', ' ')
            if currentStaff.startswith('wangjinzhu') or (currentStaff.startswith('chelijun') and fixedBy not in self.MEMBERS.keys()) or '【需求单】' in description:
                logging.info("Skipped issue from IDMS: Staff %s, FixedBy %s, %s" % (currentStaff, fixedBy, description))
                continue
            else:
                issueObj = Issue(issue)
                self.idmsIssueList.append(issueObj)
                if currentStaff.startswith('chelijun'):
                    self.MEMBERS[fixedBy].append(issueObj)
                else:
                    self.MEMBERS[currentStaff].append(issueObj)
        logging.info('%s issues fetched from IDMS.' % str(len(self.idmsIssueList)))

    def getIssuesOfMember(self, name):
        return self.MEMBERS.get(name)

    def getAllIssuesOfAllMembers(self):
        return self.MEMBERS

    def getIssueList(self):
        return self.idmsIssueList

    def getIssueNumList(self):
        return [issue.number for issue in self.idmsIssueList]

    def getIssueCountOfMember(self, name):
        return len(self.MEMBERS.get(name)) if self.MEMBERS.get(name) else 0

    def getTotalIssueCount(self):
        return len(self.idmsIssueList)

    def getMemberIssueCountMap(self):
        re = {}
        for member, issueList in self.MEMBERS.items():
            re[member] = len(issueList)
        return re

    def getIssueByNumber(self, number):
        for issue in self.idmsIssueList:
            if issue.number == number:
                return issue