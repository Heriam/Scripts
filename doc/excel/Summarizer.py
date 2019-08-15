# 仅支持.xlsx格式文件
# 支持同时选择多个数据源表到商务总表

import xlwings as xw
from xlwings.constants import Direction
import os, re, sys, time
import random

DIR = '.'
DATE = time.strftime("%Y/%m/%d", time.localtime())
PRINT_INTRO = True
WORD = 'COCO'
NICKNAME = '您好'
SINK_BOOK_NAME_PATTERN = '.*商户总表.*\.xlsx'
SOURCE_BOOK_NAME_PATTERN = '.*聚龙理财放款审批表.*\.xlsx'
NEW_FILE_SAVE_AS = './商户总表-%s.xlsx' % DATE.replace('/', '-')
COMPANY_NAME_COLUMN = 'C'
COMPANY_START_ROW = 4
COMPANY_START_COLUMN = 'A'
COMPANY_STOP_COLUMN = 'N'
DST_START_ROW = 3
DST_STOP_COLUMN = 'W'
SUM_COLUMNS = ['E', 'H', 'I', 'L', 'R']
SUMMARY_LABEL = '合计：'
DATE_COLUMN = 'O'
SERVICE_FEE_COLUMN = 'P'
DURATION_COLUMN = 'G'
SERVICE_FEE_VALUE_COLUMN = 'R'
ACTUAL_PAID_MONEY_COLUMN = 'L'


def set_date(rang, column, sheet):
    rang[ord(column)-ord(COMPANY_START_COLUMN)].value = DATE


def set_service_fee(rang, column, sheet):
    dst_grid = rang[ord(column) - ord(COMPANY_START_COLUMN)]
    last_row = int (sheet.range('%s:%s' % (COMPANY_START_COLUMN, COMPANY_START_COLUMN)).end(Direction.xlDown).get_address(False,False)[1:])
    durations = sheet.range('%s:%s' % (DURATION_COLUMN, DURATION_COLUMN))[:last_row].value
    duration = rang[ord(DURATION_COLUMN)-ord(COMPANY_START_COLUMN)].value
    # not first time
    if duration in durations:
        if duration < 30:
            dst_grid.value = '0.5%'
        elif 30 == duration:
            dst_grid.value = '1%'
        elif 60 == duration:
            dst_grid.value = '2%'
        elif 90 == duration:
            dst_grid.value = '3%'
        elif 180 == duration:
            dst_grid.value = '4%'
        else:
            raise ValueError('未定义的借贷期限: %s' % duration)
    # first time
    else:
        if duration < 30:
            dst_grid.value = '4.5%'
        elif 30 == duration:
            dst_grid.value = '5%'
        elif 60 == duration:
            dst_grid.value = '6%'
        elif 90 == duration:
            dst_grid.value = '7%'
        elif 180 == duration:
            dst_grid.value = '8%'
        else:
            raise ValueError('未定义的借贷期限: %s' % duration)


def set_service_fee_value(rang, column, sheet):
    service_fee_rate = rang[ord(SERVICE_FEE_COLUMN)-ord(COMPANY_START_COLUMN)].get_address(False,False)
    actual_paid_money = rang[ord(ACTUAL_PAID_MONEY_COLUMN)-ord(COMPANY_START_COLUMN)].get_address(False,False)
    rang[ord(column) - ord(COMPANY_START_COLUMN)].formula = '=%s*%s' % (service_fee_rate, actual_paid_money)


FUNC_DIST = {
    DATE_COLUMN: set_date,
    SERVICE_FEE_COLUMN: set_service_fee,
    SERVICE_FEE_VALUE_COLUMN: set_service_fee_value
}


def print_intro():
    allChar = []
    for y in range(12, -12, -1):
        lst = []
        lst_con = ''
        for x in range(-30, 30):
            formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if formula <= 0:
                lst_con += WORD[(x) % len(WORD)]
            else:
                lst_con += ' '
        lst.append(lst_con)
        allChar += lst
    print('\n'.join(allChar))


def get_file_list():
    file_list = os.listdir(DIR)
    file_list.sort()
    return file_list


def print_file_list():
    print('%s，在当前目录找到下列文件:' % NICKNAME)
    file_list = get_file_list()
    for i in range(len(file_list)):
        print('[%s] %s' % (i, file_list[i]))


def select_sink_book():
    file_list = get_file_list()
    number = input('%s，请告诉我商务总表的文件序号(若不存在输入exit退出):' % NICKNAME)
    if number == 'exit':
        sys.exit(0)
    if not number.isdigit():
        print('%s, 您输入的不是合法数字，请检查后重新输入' % NICKNAME)
        return select_sink_book()
    else:
        number = int(number)
    if number >= len(file_list):
        print('%s, 您指定的文件序号不存在，请检查后重新输入' % NICKNAME)
        return select_sink_book()
    elif not file_list[number].endswith(r'.xlsx'):
        print('%s, 您指定的文件格式不支持，请检查后重新输入' % NICKNAME)
        return select_sink_book()
    else:
        return file_list[number]


def select_source_book_list():
    source_book_list = []
    file_list = get_file_list()
    number_list_str = input('%s，请告诉我数据源表格的文件序号，多个文件请用空格隔开(若不存在输入exit退出):' % NICKNAME)
    if number_list_str == 'exit':
        sys.exit(0)
    number_list = number_list_str.split(' ')
    for number in number_list:
        if not number.isdigit():
            print('%s, 您输入的%s不是合法数字，请检查后重新输入' % (NICKNAME, number))
            return select_source_book_list()
        else:
            number = int(number)
        if number >= len(file_list):
            print('%s, 您指定的文件序号%s不存在，请检查后重新输入' % (NICKNAME, number))
            return select_source_book_list()
        elif not file_list[number].endswith(r'.xlsx'):
            print('%s, 您指定的文件%s格式不支持，请检查后重新输入' % (NICKNAME, number))
            return select_source_book_list()
        else:
            source_book_list.append(file_list[number])
    return source_book_list


def confirm_loaded_files(sink_book, source_book_list):
    confirm = input('%s，请确认是不是要将%s的数据导入到【%s】呀? [1]是 [2]重新手动选择 [3]退出 :' % (NICKNAME, ','.join(['【%s】' % f for f in source_book_list]), sink_book))
    if confirm == '3':
        sys.exit(0)
    if confirm == '1':
        return sink_book, source_book_list
    elif confirm == '2':
        print_file_list()
        return confirm_loaded_files(select_sink_book(), select_source_book_list())
    else:
        print('%s, 您指定选项%s不存在，请检查后重新输入' % (NICKNAME, confirm))
        return confirm_loaded_files(sink_book, source_book_list)


def load_files():
    sink_book = None
    source_book_list = []

    file_list = get_file_list()
    for file_name in file_list:
        if re.match(SINK_BOOK_NAME_PATTERN, file_name):
            sink_book = file_name
            continue
        if re.match(SOURCE_BOOK_NAME_PATTERN, file_name):
            source_book_list.append(file_name)

    if not (sink_book and source_book_list):
        print('%s, 自动加表格失败，请手工指定' % NICKNAME)
        sink_book = select_sink_book()
        source_book_list = select_source_book_list()

    return confirm_loaded_files(sink_book, source_book_list)


def validate_source_book_list(source_book_list):
    return True


def validate_sink_book(sink_book):
    return True


def import_sheet(src_sheet_obj, sink_book_obj):
    unsaved_ranges = []
    color = (random.randint(150,255), random.randint(150,255), random.randint(150,255))
    row = COMPANY_START_ROW
    sheet_name_list = [sheet.name for sheet in sink_book_obj.sheets]
    while src_sheet_obj.range('%s%s' % (COMPANY_NAME_COLUMN, row)).value:
        company_name = src_sheet_obj.range('%s%s' % (COMPANY_NAME_COLUMN,row)).value
        if company_name in sheet_name_list:
            row_data = src_sheet_obj.range('%s%s:%s%s' % (COMPANY_START_COLUMN, row, COMPANY_STOP_COLUMN, row)).value
            dst_sheet = sink_book_obj.sheets[company_name]
            dst_row = DST_START_ROW
            while dst_sheet.range('%s%s' % (COMPANY_NAME_COLUMN, dst_row)).value == company_name:
                dst_row += 1
                continue
            dst_sheet.api.Rows(dst_row).Insert()
            new_range = dst_sheet.range('%s%s:%s%s' % (COMPANY_START_COLUMN, dst_row, DST_STOP_COLUMN, dst_row))
            new_range.value = row_data
            new_range.color = color
            for key, value in FUNC_DIST.items():
                value(new_range, key, dst_sheet)
            print('导入第%s行%s数据' % (row, row_data[3]))
            unsaved_ranges.append(new_range)
            while dst_sheet.range('%s%s' % (COMPANY_START_COLUMN, dst_row)).value != SUMMARY_LABEL:
                dst_row += 1
                continue
            for column in SUM_COLUMNS:
                dst_sheet.range('%s%s' % (column, dst_row)).formula = '=SUM(%s%s:%s%s)' % (column, DST_START_ROW, column, dst_row-1)
        else:
            print('%s, 发现未知公司：%s，数据导入失败，请勿保存文件' % (NICKNAME, company_name))
            sys.exit(0)
        row += 1

    return unsaved_ranges


def import_data():
    unsaved_changes = []
    sink_book, source_book_list = load_files()
    sink_book_obj = xw.Book(sink_book)
    for src_book in source_book_list:
        src_sheet_obj = xw.Book(src_book).sheets[0]
        print('----------------------正在导入%s----------------------' % src_book)
        unsaved_changes.append(import_sheet(src_sheet_obj, sink_book_obj))
    sink_book_obj.save(NEW_FILE_SAVE_AS)
    input('恭喜亲爱的%s, 数据导入完成, 请按任意键退出 ...' % NICKNAME)


if __name__ == '__main__':
    print_intro()
    import_data()






