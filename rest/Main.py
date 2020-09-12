#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, traceback, datetime
sys.path.append('D:\My_Code')
from confluence.ConfluenceIssues import ConfluenceIssues
from idms.IDMSIssues import IDMSIssues
from emails import EmailBox
import json, logging
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log.txt",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)

if __name__ == '__main__':
    succeeded = True
    emailBox = EmailBox.EmailBox()
    mailBody = None
    idmsIssues = None
    response = None
    statistics = None

    try:
        idmsIssues = IDMSIssues()
        confluenceIssues = ConfluenceIssues()
        confluenceIssues.update(idmsIssues)
        confluenceIssues.sort()
        response = confluenceIssues.push()
        succeeded = response.status_code == 200
        mailBody = confluenceIssues.memberIssueCountHTML + confluenceIssues.getHTMLStr() + confluenceIssues.projectHtmlStr

        # 提醒日报
        if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 0:
            emailBox.remind_report_absent_member()
    except:
        traceback.print_exc()
        emailBox.send_email(EmailBox.TO_HAO_EMAIL, 'IDMS2Confluence Failed', traceback.format_exc())
        sys.exit(0)

    if succeeded:
        if datetime.datetime.now().hour == 23 and datetime.datetime.now().minute == 0:
            emailBox.send_email(EmailBox.TO_GROUP_EMAIL, '[程序发送]%s网络组日报' % datetime.datetime.now().date(), mailBody)
        else:
            emailBox.send_email(EmailBox.TO_HAO_EMAIL, 'IDMS2Confluence Succeeded: %s issues' % idmsIssues.getTotalIssueCount(), mailBody)

    else:
        emailBox.send_email(EmailBox.TO_HAO_EMAIL,
                            'IDMS2Confluence Failed: HTTP %s' % response.status_code, response.content.decode("utf-8") + mailBody)