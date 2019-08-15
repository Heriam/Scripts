import xlwings as xw
import time,os,sys,re

DIR = '.'
NOW = time.localtime()
COLUMN_NAME_ROW = 1
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


class InterviewICSGenerator:
    sheet = None
    columnNameMap = {}

    def __init__(self):
        self._load_interviews()

    def _load_interviews(self):
        for filename in os.listdir(DIR):
            if re.match(".*招聘汇总\-杭州.*\.xlsx", filename):
                self.sheet = xw.Book(filename).sheets[0]
        if not self.sheet:
            print("未找到招聘汇总EXCEL表格")
            sys.exit(0)
        print(self.sheet.range().options(dict).value)

if __name__ == "__main__":
    InterviewICSGenerator()
