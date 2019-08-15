import xlwings as xw
import icalendar
import time,os,sys,re

DIR = "."
COLON = ":"
NOW = time.localtime()
COLUMN_START = "A"
COLUMN_END = "M"
COLUMN_NAME_ROW = 1
KEY_COLUMN = "C"
FILENAME_PATTERN = ".*招聘汇总\-杭州.*\.xlsx"
FILE_NOT_FOUND = "未找到招聘汇总EXCEL表格"
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
RESERVATION = "预约面试时间"
LOCATION = "预约面试地点"


class InterviewICSGenerator:
    sheet = None
    columnNames = []
    interviews = []

    def __init__(self):
        self._load_interviews()

    def _load_interviews(self):
        for filename in os.listdir(DIR):
            if re.match(FILENAME_PATTERN, filename):
                self.sheet = xw.Book(filename).sheets[0]
        if not self.sheet:
            print(FILE_NOT_FOUND)
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





if __name__ == "__main__":
    InterviewICSGenerator()
