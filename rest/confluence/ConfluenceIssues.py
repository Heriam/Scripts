#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import traceback
from json.decoder import JSONDecodeError

import requests, json, re, copy, datetime, threading
from urllib.parse import *
from requests.auth import HTTPBasicAuth
from Issue import Issue
import logging

# ----------- Logging --------------------

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log.txt",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)


class ConfluenceIssues:
    URL = 'http://10.99.216.200:8090/rest/api/content/66430?expand=body.storage'
    PROJECT_URL = 'http://10.99.216.200:8090/rest/api/content/65635?expand=body.storage'
    VERSIONURL = 'http://10.99.216.200:8090/rest/api/content/66430/history/'

    def __init__(self):
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth('j16492', 'Jh004211')
        self.htmlStr = self.session.get(self.URL).content.decode("utf-8")
        try:
            self.htmlStr = json.loads(self.htmlStr)['body']['storage']['value'].split('<hr />')[-1]
        except JSONDecodeError:
            logging.error(traceback.format_exc())
            logging.error(self.htmlStr)
            sys.exit(0)
        self.trList = [tr[:-5] for tr in
                       re.search(r'<tbody>[\s\S]+</tbody>', self.htmlStr).group(0)[7:-8].split('<tr>')]
        self.tableHead = re.search('^.*<tbody>', self.htmlStr).group(0)
        self.columnHead = '<tr>' + self.trList[1] + '</tr>'
        self.onPageIssueList = [Issue([td[:-5] for td in tr.split('<td>')[1:]], fromIDMS=False) for tr in
                                self.trList[2:]]
        self.tableTail = re.search('</tbody>.*$', self.htmlStr).group(0)
        self.version = json.loads(self.session.get(self.VERSIONURL).content.decode("utf-8"))['lastUpdated']['number']
        self.memberIssueCountHTML = ''
        self.projectHtmlStr = json.loads(self.session.get(self.PROJECT_URL).content.decode("utf-8"))['body']['storage'][
            'value']
        self.groupIssueSumTable = {}
        self.groupTotoalIssueSumList = []
        logging.info('fetched data from Confluence. Data version: %s' % str(self.version))

    def update(self, idmsIssues):
        li = []
        for issue in self.onPageIssueList:
            if issue.number not in idmsIssues.getIssueNumList():
                logging.info('removed resolved issue %s from page.' % issue.number)
            else:
                li.append(issue.update(idmsIssues.getIssueByNumber(issue.number)))
        self.onPageIssueList = copy.deepcopy(li)
        for issue in idmsIssues.getIssueList():
            if issue.number not in self.getIssueNumList():
                self.onPageIssueList.append(issue)
                logging.info('appended new issue %s on page, current staff: %s, current status: %s.' % (
                issue.number, issue.currentStaff, issue.status))
        for member, issueList in idmsIssues.MEMBERS.items():
            self.groupIssueSumTable[member] = [len(issueList), 0, 0, 0, 0, 0]
        self.memberIssueCountHTML = '<h1>问题单遗留: %s</h1><hr />' % len(
            idmsIssues.getIssueList()) + self._getGroupIssueSumTable(idmsIssues) + '<br /><h1>问题单列表</h1><hr />'

    def sort(self):
        logging.info('sorting issues by staff name.')
        self.onPageIssueList = sorted(copy.deepcopy(self.onPageIssueList), key=lambda issue: issue.responsible)

    def push(self):
        logging.info('pushing updates to Confluence. version: %s' % str(self.version + 1))
        url = 'http://10.99.216.200:8090/rest/api/content/66430'
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        body = {
            "id": "66430",
            "type": "page",
            "title": "缺陷管理",
            "space": {"key": "network"},
            "body": {
                "storage": {
                    "value": "%s" % self.memberIssueCountHTML + self.getHTMLStr(),
                    "representation": "storage"
                }
            },
            "version": {
                "number": self.version + 1,
                "minorEdit": True
            }
        }
        response = self.session.put(url=url, headers=headers, data=json.dumps(body))
        if response.status_code != 200:
            logging.error('Update Confluence Failed! HTTP %s: %s' % (response.status_code, response.content.decode("utf-8")))
            logging.error('Content to be updated: %s' % body)
        else:
            logging.info('Updated Confluence Successfully! %s: %s' % (response.status_code, response.content.decode("utf-8")))
        return response

    def getHTMLStr(self):
        content = self.tableHead + self.columnHead + ''.join(
            [issue.getHTMLStr() for issue in self.onPageIssueList]) + self.tableTail
        if '&Campus' in content:
            logging.warning('Replacing "&Campus" to " Campus" in updated content: %s' % content)
            content = content.replace('&Campus', ' Campus')
        return content

    def getIssueNumList(self):
        return [issue.number for issue in self.onPageIssueList]

    def _style_rank(self, num):
        if num <= 2:
            color = 'black'
        elif 4 > num > 2:
            color = 'orange'
        elif 6 > num >= 4:
            color = 'red'
        else:
            color = '#8B0000'
        return '<p style="color:%s;">%s</p>' % (color, num)

    def _getGroupIssueSumTable(self, idmsIssues):
        threads = []
        self.groupTotoalIssueSumList = [str(len(idmsIssues.getIssueList())),'','','','','']
        for i in range(1, 6):
            t = threading.Thread(target=self._updateDayOfResolvedIssues, args=(idmsIssues, i))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        return '<table class=\"wrapped\"><colgroup><col /><col /><col /><col /><col /><col /><col /></colgroup><tbody><tr><th>个人</th><th>当前遗留</th><th colspan=\"1\">今日解决</th><th>近两日解决</th><th>近7天解决</th><th>近30天解决</th><th>近90天解决</th></tr>' + ''.join(
            ['<tr><td>%s</td><td style="text-align:center">' % mem.split(' ')[0] + self._style_rank(cntList[0]) + '</td><td style="text-align:center">' + '</td><td style="text-align:center">'.join([str(i) for i in cntList[1:]]) + '</td></tr>' for mem, cntList in
             sorted(self.groupIssueSumTable.items(), key=lambda mem: mem[1][0], reverse=True)]) + '<tr><th>总计</th><th style="text-align:center">' + '</th><th style="text-align:center">'.join(self.groupTotoalIssueSumList) + '</th></tr></tbody></table>'

    def _updateDayOfResolvedIssues(self, idmsIssues, index):
        if index == 1:
            days = 0
        elif index == 2:
            days = 1
        elif index == 3:
            days = 7
        elif index == 4:
            days = 30
        else:
            days = 90
        endDate = str(datetime.datetime.now().date())
        startDate = str((datetime.datetime.now() - datetime.timedelta(days=days)).date())
        r = json.loads(idmsIssues.s.post(url=idmsIssues.SEARCH_URL, headers=idmsIssues.HEADERS, data=idmsIssues.SEARCH_RESOLVED_DATE_RAW.replace('{{startDate}}', startDate).replace('{{endDate}}', endDate)).content.decode("utf-8"))['aaData']
        issues = [issue for issue in r if (issue[0] != '\u3000' and re.search(r'data-defactmodifier=".*" data-submitBy', issue[0]).group(0).split('"')[1] in idmsIssues.MEMBERS.keys())]
        for issue in issues:
            fixedBy = re.search(r'data-defactmodifier=".*" data-submitBy', issue[0]).group(0).split('"')[1]
            self.groupIssueSumTable[fixedBy][index] += 1
        self.groupTotoalIssueSumList[index] = str(len(issues))
        logging.info('fetched %s resolved issues in last %s days.' % ( str(len(issues)),str(days)))
