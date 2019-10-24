import logging, os
ROOT_DIR = 'C:\\Users\\j16492\\PycharmProjects\\Scripts'
logger = logging.getLogger('REFUSE')
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename=ROOT_DIR + '\\doc\\ics\\refuse.log', encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
from emails.EmailSender import *
from jinja2 import Environment, PackageLoader
from .Constants import *
import datetime
import threading
from random import randint

os.chdir(ROOT_DIR+'\\doc\\ics')
REFUSE_STATEMENTS = [
    '感谢你对我们的认同并抽空参与面试。经过综合考量，我们已确定了最适合这个岗位的人选。\
     因此非常遗憾暂时未能有机会与你共事。这次的岗位竞争非常激烈，目前我们确实需要最符合这一岗位综合各方面需求的人选。然而，\
     我们很欣赏上次面试与你的会谈，也认为如果有适合的机会，你肯定能大展才能。相信你一定能很快找到理想的岗位。也希望以后有机会能一起共事！'
                     ]

class Rejecter:
    lock = threading.Lock()
    sent = []
    failed = []

    def newParagraph(self, str):
        return '<p style="Margin-top: 20px;Margin-bottom: 0;">%s</p>' % str

    def sendRejection(self, interview):
        with self.lock:
            with open("refusedlist", "r+") as f:
                refusedList = f.read()
                to = interview.get(EMAIL)
                candidate_name = interview.get(NAME)
                bcc = BCC
                if MARKED == interview.get(REFUSEMAIL) and to not in refusedList:
                    env = Environment(loader=PackageLoader("doc.ics"))
                    template = env.get_template("refusemail.htm")
                    candiddate_title = "先生/女士"
                    if "男" == interview.get(SEX):
                        candiddate_title = "先生"
                    elif "女" == interview.get(SEX):
                        candiddate_title = "女士"
                    subject = "新华三技术有限公司致%s%s面试反馈函" % (candidate_name, candiddate_title)
                    interview_time = interview.get(RESERVED_SLOT)
                    position_name = interview.get(TARGETED_POSITION)
                    department_name = interview.get(DEPARTMENT)
                    content = self.newParagraph('非常感谢您抽出宝贵的时间应聘新华三%s%s岗位！但是很遗憾，我们暂时没能找到合适的机会与您合作。请知悉您此次应聘的面试反馈如下：' % (department_name,position_name))
                    content += self.newParagraph('面试结论：不建议进行下一轮面试')
                    content += self.newParagraph('详细反馈：%s%s你好！%s' % (candidate_name, candiddate_title, REFUSE_STATEMENTS[randint(0, len(REFUSE_STATEMENTS)-1)]))
                    content += self.newParagraph('请您理解：此次结果不是对您表现的负面评价，而是仅出于对我们这一特定岗位招聘需求的考量。我们非常感谢您关注并应聘新华三技术有限公司，这已经给我们留下了深刻的印象。\
                    我们也希望您将这一过程视为对您个人发展和成长的宝贵经验。您的相关资料已经保存在我们的人才数据库中，今后如果还有其他适合您的职位，我们会与您联系。也欢迎您继续关注新华三的招聘信息，我们期待着您将来加入我们。')
                    body = template.render(
                        position_name=position_name,
                        department_name=department_name,
                        candidate_name=candidate_name,
                        candiddate_title=candiddate_title,
                        interview_time=interview_time,
                        letter_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        letter_content=content,
                        last_wishes="祝您在未来工作和生活中一切顺利！",
                        sender_name=SENDER_NAME
                    )
                    sendEmail(to, bcc, subject, body)
                    f.write(candidate_name + ' ' + to + '\n')
                    logger.info(" √ 发送 %s:%s" % (candidate_name,to))
                    self.sent.append(candidate_name + ' ' + to)
                else:
                    logger.info(" o 跳过 %s:%s" % (candidate_name, to))

    def getLock(self):
        return self.lock

    def getSent(self):
        return self.sent

    def getFailed(self):
        return self.failed

    def addFailed(self, failedEntry):
        self.failed.append(failedEntry)