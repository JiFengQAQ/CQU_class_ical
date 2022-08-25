# coding: utf-8
# Author: SunsetYe
# Website: SunsetYe <github.com/sunsetye66>
# Contact: SunsetYe <me # sunsetye.com>
import sys


def gen_week():
    from week_generate_tool import GenerateWeeks
    process = GenerateWeeks()
    process.set_attribute()
    process.main_process()


def read_excel():
    from excel_reader import ExcelReader
    process = ExcelReader()
    process.main()


def gen_ical():
    from ical_generator import GenerateCal
    process = GenerateCal()
    process.set_attribute()
    process.main_process()


def main(i):
    inform_text1 = '''
欢迎使用CQU课表转日历工具!
有关具体的使用说明, 请阅读 README.md . 
一般情况下, 请先使用功能1, 再使用功能2即可. '''
    if i == 1:
        print(inform_text1)
    inform_text2 = '''======================================
输入 1 进入[Excel 读取工具];
输入 2 进入[iCal 生成工具];
输入 4 进入[周数指示器 生成程序];
输入 0 退出, 祝您使用愉快 ~'''
    print(inform_text2)
    func = input("请输入要进入的功能:")
    if func == "0":
        sys.exit()
    elif func == "4":
        gen_week()
    elif func == "1":
        read_excel()
    elif func == "2":
        gen_ical()
    else:
        print("emmmmmmmmm...")
        sys.exit()


if __name__ == '__main__':
    i = 1
    while True:
        main(i)
        print("", end="\n")
        i += 1
