import logging, os
ROOT_DIR = 'C:\\Users\\j16492\\PycharmProjects\\Scripts'
logger = logging.getLogger('EMAIL')
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename=ROOT_DIR + '\\doc\\ics\\email.log', encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
from emails.EmailSender import *
from jinja2 import Environment, PackageLoader
from .Constants import *
import datetime
import threading

os.chdir(ROOT_DIR+'\\doc\\ics')


class Invitor:
    lock = threading.Lock()
    sent = []
    failed = []

    def sendInvitation(self, interview):
        with self.lock:
            with open("mailedlist", "r+") as f:
                mailedList = f.read()
                to = interview.get(EMAIL)
                candidate_name = interview.get(NAME)
                bcc = "zhou.huan@h3c.com"
                if "Y" == interview.get(INVITEMAIL) and to not in mailedList:
                    env = Environment(loader=PackageLoader("doc.ics"))
                    template = env.get_template("invitemail.htm")
                    candiddate_title = "先生/女士"
                    if "男" == interview.get(SEX):
                        candiddate_title = "先生"
                    elif "女" == interview.get(SEX):
                        candiddate_title = "女士"
                    subject = "新华三技术有限公司致%s%s面试邀请函" % (candidate_name, candiddate_title)
                    INDIVIDUAL_CAMPUS_IN = "在面试当天或之前您将会通过短信收到一个访客二维码，届时请您凭此二维码从江二路的园区南门接待室处领取来宾卡进入园区。"
                    INDIVIDUAL_AFTER_CAMPUS_IN = "进入园区后，请您联系通知我们的面试接口人%s，然后在1号楼的一楼大厅北侧沙发区就坐稍作休息并耐心等候。" % interview.get(CONTACT)
                    SESSION_CAMPUS_IN = "在面试当天，请您凭此邮件（您可以打印出纸质版的邮件，手机出示电子版的亦可）在江二路的园区南门接待室处进行来访登记后进入园区。"
                    SESSION_AFTER_CAMPUS_IN = "进入园区后，请您前往2号楼员工食堂的1层或者2层社招专场签到处签到，如果您找不到签到处，可以电话联系我们的面试接口人" + interview.get(
                        CONTACT)
                    campus_in = INDIVIDUAL_CAMPUS_IN
                    after_campus_in = INDIVIDUAL_AFTER_CAMPUS_IN
                    interview_time = interview.get(RESERVED_SLOT)
                    position_name = interview.get(TARGETED_POSITION)
                    if "专场" in interview.get(RESERVED_SLOT):
                        campus_in = SESSION_CAMPUS_IN
                        after_campus_in = SESSION_AFTER_CAMPUS_IN
                    body = template.render(
                        position_name=position_name,
                        department_name=interview.get(DEPARTMENT),
                        candidate_name=candidate_name,
                        candiddate_title=candiddate_title,
                        interview_time=interview_time,
                        campus_in=campus_in,
                        after_campus_in=after_campus_in,
                        letter_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        last_wishes="祝您生活愉快，",
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