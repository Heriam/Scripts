import sys

ROOT_DIR = 'C:\\Users\\j16492\\PycharmProjects\\Scripts'
sys.path.append(ROOT_DIR)
from comm.email.EmailSender import *
from jinja2 import Environment, PackageLoader
from doc.ics.Constants import *
import datetime


def sendInvitation(interview):
    with open("mailedlist", "r+") as f:
        mailedList = f.read()
        to = interview.get(EMAIL)
        bcc = "zhou.huan@h3c.com"
        if "待发" == interview.get(INVITEMAIL) and to not in mailedList:
            subject = "新华三技术有限公司社招面试邀请函"
            env = Environment(loader=PackageLoader("doc.ics"))
            template = env.get_template("index.htm")
            candiddate_title = "先生/女士"
            if "男" == interview.get(SEX):
                candiddate_title = "先生"
            elif "女" == interview.get(SEX):
                candiddate_title = "女士"
            INDIVIDUAL_CAMPUS_IN = "在面试当天或之前您将会通过短信收到一个访客二维码，届时请您凭此二维码从江二路的园区南门接待室处领取来宾卡进入园区。"
            INDIVIDUAL_AFTER_CAMPUS_IN = "进入园区后，请您联系通知我们的面试接口人%s，然后在1号楼的一楼大厅北侧沙发区就坐稍作休息并耐心等候。" % interview.get(CONTACT)
            SESSION_CAMPUS_IN = "在面试当天，请您凭此邮件（您可以打印出纸质版的邮件，手机出示电子版的亦可）在江二路的园区南门接待室处进行来访登记后进入园区。"
            SESSION_AFTER_CAMPUS_IN = "进入园区后，请您前往2号楼员工食堂的1层或者2层社招专场签到处签到，如果您找不到签到处，可以电话联系我们的面试接口人" + interview.get(
                CONTACT)
            campus_in = INDIVIDUAL_CAMPUS_IN
            after_campus_in = INDIVIDUAL_AFTER_CAMPUS_IN
            if "专场" in interview.get(RESERVED_SLOT):
                campus_in = SESSION_CAMPUS_IN
                after_campus_in = SESSION_AFTER_CAMPUS_IN
            body = template.render(
                position_name=interview.get(TARGETED_POSITION),
                department_name=interview.get(DEPARTMENT),
                candidate_name=interview.get(NAME),
                candiddate_title=candiddate_title,
                interview_time=interview.get(RESERVED_SLOT),
                sender_email=SENDER,
                campus_in=campus_in,
                after_campus_in=after_campus_in,
                letter_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            sendEmail(to, bcc, subject, body)
            f.write(interview.get(NAME) + ' ' + to + '\n')
