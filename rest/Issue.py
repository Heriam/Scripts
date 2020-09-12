#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import logging, datetime
from emails import EmailBox

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="log.txt",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)


class Issue:

    REVIEW_TEMPLATE = '''
    <b>9.1	操作指导</b><br />
        1、	审核人需要取配置库上修改后的文件进行检查，检查是否合入问题单指定的版本。<br />
        2、	审核人需要检查修改的正确性，在技术上把关。<br />
        3、	审核人需要检查修改实施步骤所要求提供的交付件是否都符合规范要求，不符合要求者打回重新修改。<br />
        4、	简化流程的问题单，审核通过后直接走到“G确认关闭”环节。<br />
        5、	“跨产品复制单”的开发定位/审核/修改实施/修改审核 等环节，只需要说明同原单即可，随原问题单一并归档。<br />
        <br />
    <b>9.2	管理规范</b><br />
        1、	审核人必须按照9.3审核模板进行审核；并把检查结果附在审核环节。<br />
        2、	系统测试阶段，简化流程的问题单在开发内部联调版本发布前，都应该走到“问题确认”。<br />
        3、	必须保证修改人已把代码修改合入到问题单中指定的合入版本。<br />
        4、	此步骤原则上允许停留1个工作日。<br />
        <br />
    <b>9.3 审核模板</b><br />
        #  自检查Checklist | 审核结果<br />
        1、 合入正确的版本分支	<br />
        2、 合入的代码是否正确	<br />
        3、 没有夹带合入代码	<br />
        4、 修改文件清单是否正确（是否全路径、文件名是否正确）	<br />
        5、 有代码比较文件	<br />
        6、 有正确的工具检查结果	<br />
        7、 是否组织代码走读	<br />
        8、 按照模板编写测试建议	<br />
        9、按照模板提供验证报告	<br />
    '''

    def __init__(self, issue, fromIDMS=True):
        self.number = re.search('>\d+<', issue[1]).group(0)[1:-1] if fromIDMS else issue[1]
        self.description = issue[2]
        self.status = issue[3]
        self.currentStaff = issue[4]
        self.version = issue[7] if fromIDMS else issue[5]
        self.severity = issue[8] if fromIDMS else issue[6]
        self.heldFor = issue[9] if fromIDMS else issue[7]
        self.submittedOn = issue[10] if fromIDMS else issue[8]
        self.submittedBy = issue[11] if fromIDMS else issue[9]
        self.fixedBy = issue[12] if fromIDMS else issue[10]
        self._tasks = '' if fromIDMS else issue[0]
        self._remarks = '' if fromIDMS or len(issue) < 12 else issue[11]
        self.responsible = self.fixedBy if self.currentStaff.startswith('chelijun') else self.currentStaff
        self._reviewRemind() if fromIDMS else None

    def getOnPageList(self):
        isOld = datetime.datetime.fromisoformat(self.submittedOn) <= datetime.datetime.fromisoformat('2020-08-25')
        return [self._tasks, self.number, self.description, self.status, self.currentStaff, self.version,
                               self.severity, self.heldFor, '<p style="color:red;">'+ self.submittedOn + '</p>' if isOld else self.submittedOn, self.submittedBy, self.fixedBy,
                               self._remarks]

    def getHTMLStr(self):
        return '<tr>%s</tr>' % ''.join(['<td>%s</td>' % col for col in self.getOnPageList()])

    def __str__(self):
        return str(self.__dict__)

    def update(self, issue):
        if self.number != issue.number:
            logging.error('issue %s cannot be updated by another issue %s.' % (self.number, issue.number))
            return
        else:
            if self.status != issue.status:
                logging.info('updating issue %s status: %s -> %s' % (self.number, self.status, issue.status))
            self.description = issue.description
            self.status = issue.status
            self.currentStaff = issue.currentStaff
            self.version = issue.version
            self.severity = issue.severity
            self.heldFor = issue.heldFor
            self.submittedOn = issue.submittedOn
            self.submittedBy = issue.submittedBy
            self.fixedBy = issue.fixedBy
            self.responsible = issue.responsible
        return self

    def _reviewRemind(self):
        now = datetime.datetime.now()
        if "实施审核" in self.status and now.hour in [8,11,14,17,20] and now.minute == 0:
            email = EmailBox.EmailBox()
            email_addr = email.find_email_address_by_name(self.currentStaff)
            logging.info('Reminding %s to review issue %s.' % (email_addr, self.number))
            email.send_email([email_addr], "[提醒]请尽快审核问题单%s" % self.number, self.REVIEW_TEMPLATE, EmailBox.TO_HAO_EMAIL)