import xlwings as xw
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import os, sys, re, json, uuid, pytz
import traceback

ROOT_DIR = 'C:\\Users\\j16492\\PycharmProjects\\Scripts'
sys.path.append(ROOT_DIR)
from npl.TimeNormalizer import TimeNormalizer
import logging

EXCEL_DIR = "E:\\OutlookAttachments\\"
COLON = ":"
TIMEZONE = pytz.timezone("Asia/Shanghai")
NOW = datetime.now(tz=TIMEZONE)
COLUMN_START = "A"
COLUMN_END = "M"
COLUMN_NAME_ROW = 1
KEY_COLUMN = "C"
FILENAME_PATTERN = ".*招聘汇总\-杭州.*\.xlsx"
DEPARTMENT_SEERANALYZER = "智能引擎"

DUPLICATION_CHECK = "匹配"
DEPARTMENT = "应聘部门"
MOBILE = "手机"
NAME = "姓名"
SEX = "性别"
DEGREE = "学历"
MAJOR = "专业"
UNIVERSITY = "学校"
TARGETED_POSITION = "应聘职位"
EMAIL = "EMAIL"
RESUME = "简历来源"
RESERVED_SLOT = "预约面试时间"
LOCATION = "预约面试地点\n北京/杭州/合肥"

logger = logging.getLogger('ICS')
logger.setLevel(logging.DEBUG)
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)
formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
fh = logging.FileHandler(filename=ROOT_DIR + '\\doc\\ics\\ics.log', encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


class InterviewICSGenerator:
    sheet = None
    columnNames = []
    interviews = []
    calendar = Calendar()

    def __init__(self):
        self.calendar.add("x-wr-calname", "面试日程")
        self._load_interviews()

    def _load_interviews(self):
        for filename in os.listdir(EXCEL_DIR):
            if re.match(FILENAME_PATTERN, filename):
                self.sheet = xw.Book(EXCEL_DIR + filename).sheets[0]
        if not self.sheet:
            logger.warning("未找到招聘汇总EXCEL表格")
            sys.exit(0)
        self.columnNames = self.sheet.range(
            COLUMN_START + str(COLUMN_NAME_ROW) + COLON + COLUMN_END + str(COLUMN_NAME_ROW)).value
        row = COLUMN_NAME_ROW + 1
        while self.sheet.range(KEY_COLUMN + str(row)).value:
            interview = {}
            for i in range(len(self.columnNames)):
                interview[self.columnNames[i]] = \
                self.sheet.range(COLUMN_START + str(row) + COLON + COLUMN_END + str(row)).value[i]
            if DEPARTMENT_SEERANALYZER in interview.get(DEPARTMENT):
                self.interviews.append(interview)
            row += 1

    def _format_date(self, match):
        lent = len([word for word in re.split(r"[./\-年月]", match.group()) if word])
        text = match.group()
        if lent == 3:
            text = re.sub("[./\-年]", "年", text, count=1)
            text = re.sub("[./\-月]", "月", text, count=1)
        elif lent == 2:
            text = re.sub("[./\-月]", "月",text, count=1)
        if not re.search("[日号]$", text):
            text = text + "日"
        return text

    def generate_ics(self):
        interview = "not initialized"
        timestamp = "not initialized"
        try:
            for interview in self.interviews:
                #编辑时间
                slotOriginal = interview.get(RESERVED_SLOT)
                slotStripped = re.sub("[这本]?下*个?(星期|周|礼拜)[一二三四五六日]", "", slotOriginal)
                slotFormated = re.sub("((20)?[1-2][0-9][./\-年])?((10|11|12)|(0?[1-9]))[./\-月](([12][0-9])|(30|31)|(0?[1-9]))[日号]?",
                                      self._format_date, slotStripped)
                slotReserved = re.sub("[`~!@#$%^&*()_+=|{}';,\[\].<>?！￥…（）/《》【】‘；”“’。，、？]", " ", slotFormated)
                timestamp = TimeNormalizer().parse(target=slotReserved,
                                                   timeBase=NOW.replace(month=1, day=1, hour=0, second=0,
                                                                        microsecond=0).strftime("%Y-%m-%d %H:%M:%S"))
                err = eval(timestamp).get("error")
                if err:
                    logger.error(err + " " + str(interview))
                    continue
                parsedTime = eval(timestamp).get("timestamp") or eval(timestamp).get("timespan")[0]
                dtstart = TIMEZONE.localize(datetime.strptime(parsedTime, "%Y-%m-%d %H:%M:%S")).astimezone(tz=pytz.utc)
                dtend = dtstart + timedelta(hours=2)
                #编辑基本信息
                location = interview.pop(LOCATION)
                location = location if location else "杭州"
                interview[LOCATION.split("\n")[0]] = location
                interview[MOBILE] = int(interview[MOBILE])
                description = json.dumps(interview, indent=0, sort_keys=True, ensure_ascii=False)
                description = re.sub("[\"{},]", "", description)
                summary = interview.get(NAME) + " " + interview.get(UNIVERSITY)
                #新建事件
                event = Event()
                event.add("uid", "%s:%s:%s" % (dtstart.timestamp(), interview.get(MOBILE), uuid.uuid4()))
                event.add("summary", summary)
                event["dtstart"] = dtstart.strftime("%Y%m%dT%H%M%SZ")
                event["dtend"] = dtend.strftime("%Y%m%dT%H%M%SZ")
                event.add("description", description)
                event.add("location", location)
                self.calendar.add_component(event)
                logger.info("%s %s %s -> %s -> %s" % (
                interview.get(DEPARTMENT), interview.get(NAME), slotOriginal, slotReserved, dtstart))
            with open(ROOT_DIR + '\\doc\\ics\\interview.ics', 'wb') as f:
                f.write(self.calendar.to_ical())
                f.close()
        except Exception as err:
            logger.error(str(err) + str(traceback.print_exc() or " "))
            logger.error("Interview: "+str(interview))
            logger.error("Time: "+str(timestamp))

        finally:
            if xw.apps.active:
                xw.apps.active.quit()


if __name__ == "__main__":
    try:
        InterviewICSGenerator().generate_ics()
    except Exception as err:
        import traceback
        logger.error(str(err) + str(traceback.print_exc() or " "))
    finally:
        if xw.apps.active:
            xw.apps.active.quit()
