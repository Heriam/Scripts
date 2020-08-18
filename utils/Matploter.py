import matplotlib.pyplot as plt
import datetime
import xlwings as xw

dates = []
roundDelays = []
roundTotals = []
time = datetime.datetime.now()

if __name__ == '__main__':
    excel = xw.Book()
    sheet = excel.sheets[0]
    new_range = sheet.range('')
    excel.save('output')