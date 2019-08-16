import xlwings as xw
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import os,sys,re,json,uuid
from npl.TimeNormalizer import TimeNormalizer
import logging
logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="ics.log",
    format="[%(asctime)s][%(levelname)s]:%(message)s"
)

DIR = "."
COLON = ":"
NOW = datetime.now()
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


class InterviewICSGenerator:
    sheet = None
    columnNames = []
    interviews = []
    calendar = Calendar()
    logger = None

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.calendar.add("x-wr-calname", "面试日程")
        self._load_interviews()

    def _load_interviews(self):
        for filename in os.listdir(DIR):
            if re.match(FILENAME_PATTERN, filename):
                self.sheet = xw.Book(filename).sheets[0]
        if not self.sheet:
            self.logger.warning("未找到招聘汇总EXCEL表格")
            sys.exit(0)
        self.columnNames = self.sheet.range(COLUMN_START+str(COLUMN_NAME_ROW)+COLON+COLUMN_END+str(COLUMN_NAME_ROW)).value
        row = COLUMN_NAME_ROW+1
        while self.sheet.range(KEY_COLUMN + str(row)).value:
            interview = {}
            for i in range(len(self.columnNames)):
                interview[self.columnNames[i]] = self.sheet.range(COLUMN_START+str(row)+COLON+COLUMN_END+str(row)).value[i]
            if DEPARTMENT_SEERANALYZER in interview.get(DEPARTMENT):
                self.interviews.append(interview)
            row+=1

    def _format_date(self, match):
        text = re.sub("[\.\/\-]", "月", match.group())
        if not re.search("[日号]$", text):
            text = text + "日"
        return text

    def generate_ics(self):
        for interview in self.interviews:
            slotOriginal = interview.get(RESERVED_SLOT)
            slotStripped = re.sub("[这本]?下*个?(星期|周|礼拜)[一二三四五六日]", "", slotOriginal)
            slotFormated = re.sub("((10|11|12)|(0?[1-9]))[\.\/\-月](([12][0-9])|(30|31)|(0?[1-9]))[日号]?",self._format_date, slotStripped)
            slotReserved = re.sub("[`~!@#$%^&*()_+=|{}';,\[\].<>/?！￥…（）《》【】‘；”“’。，、？]", "", slotFormated)
            timestamp = TimeNormalizer().parse(target=slotReserved,timeBase=NOW.replace(month=1,day=1,hour=0,second=0,microsecond=0).strftime("%Y-%m-%d %H:%M:%S"))
            parsedTime = eval(timestamp).get("timestamp")

            dtstart = datetime.strptime(parsedTime, "%Y-%m-%d %H:%M:%S")
            dtend = dtstart + timedelta(hours=2)
            summary = interview.get(NAME) + " " + interview.get(UNIVERSITY)
            location = interview.pop(LOCATION)
            location = location if location else "杭州"
            interview[LOCATION.split("\n")[0]] = location
            description = json.dumps(interview, indent=0, sort_keys=True, ensure_ascii=False)
            description = re.sub("[\"{},]", "", description)

            event = Event()
            event.add("uid", "%s:%s:%s"%(dtstart.timestamp(),interview.get(MOBILE),uuid.uuid4()))
            event.add("summary", summary)
            event["dtstart"] = dtstart.strftime("%Y%m%dT%H%M%SZ")
            event["dtend"] = dtend.strftime("%Y%m%dT%H%M%SZ")
            event.add("description", description)
            event.add("location", location)
            self.calendar.add_component(event)
            self.logger.info("%s %s %s -> %s -> %s" % (interview.get(DEPARTMENT),interview.get(NAME),slotOriginal,slotReserved,dtstart))
        with open('interview.ics', 'wb') as f:
            f.write(self.calendar.to_ical())
            f.close()

if __name__ == "__main__":
    InterviewICSGenerator().generate_ics()
