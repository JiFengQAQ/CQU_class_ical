# coding: utf-8
# Author: SunsetYe inherited from ChanJH
# Website: ChanJH <chanjh.com>, SunsetYe <github.com/sunsetye66>
# Contact: SunsetYe <me # sunsetye.com>
# class info: classInfo: "" 时间的json
# design: class[0] = {className:"", startWeek:"", endWeek:"", weekStatus:,
# weekday:"", classTimeId:, classroom:"", teacher:""}

import sys
import json
import xlrd
import os
from random import randint
from cqu_config import classTimeTranslate


class ExcelReader:
    def __init__(self):
        # 读取备注细节的配置文件
        try:
            with open("note_config.json", 'r', encoding='UTF-8') as f:
                self.note_config = json.loads(f.read())
                f.close()
        except:
            print("备注细节配置文件 note_config.json 似乎有点问题")
            sys.exit()

        # 指定信息在 xls 表格内的列数，第一列是第 0 列。
        self.config = dict()
        self.config["ClassName"] = 0
        self.config["ClassTime"] = 2
        self.config["Classroom"] = 3
        self.config["isClassSerialEnabled"] = [
            self.note_config["isAddClassSerial"], 1]
        self.config["isClassTeacherEnabled"] = [
            self.note_config["isAddTeacher"], 4]

        # 读取 excel 文件
        try:
            self.data = xlrd.open_workbook('classInfo.xls')
        except FileNotFoundError:
            print("文件不存在，请确认是否将课程信息前的 temp_ 去掉！")
            sys.exit()
        self.table = self.data.sheets()[0]
        # 基础信息
        self.numOfRow = self.table.nrows  # 获取行数,即课程数
        self.numOfCol = self.table.ncols  # 获取列数,即信息量
        self.classList = list()

    def confirm_conf(self):
        # 与用户确定配置内容
        print("--------------------------------------")
        print("Excel 解析器:\n若自行修改过 Excel 表格结构, 请检查. ")
        print("若要设定是否显示课程编号, 是否显示任课教师，请修改 note_config.json")
        print("ClassName: ", self.config["ClassName"])
        print("ClassTime: ", self.config["ClassTime"])
        print("Classroom: ", self.config["Classroom"])

        print("isClassSerialEnabled: ",
              self.config["isClassSerialEnabled"][0], end="")
        if self.config["isClassSerialEnabled"][0]:
            print(" ,", "Serial: ", self.config["isClassSerialEnabled"][1])

        print(" isClassTeacherEnabled: ",
              self.config["isClassTeacherEnabled"][0], end="")
        if self.config["isClassTeacherEnabled"][0]:
            print(" ,", "Teacher: ", self.config["isClassTeacherEnabled"][1])

        option = input("回车继续, 输入其他内容退出: ")
        if option:
            return 1
        else:
            return 0

    def load_data(self):
        i = 2  # 去掉表头
        _i = 0  # 输出所用行标
        while i < self.numOfRow:
            _i = len(self.classList)
            singleClassList: list = classTimeTranslate(
                self.table.cell(i, self.config["ClassTime"]).value)
            if singleClassList[0]["WholeWeek"] == True:  # 暂时没有能力处理整周课程
                i += 1
                continue
            self.classList.extend(singleClassList)
            for __i in range(_i, len(self.classList)):
                self.classList[__i].setdefault(
                    "ClassName", self.table.cell(i, self.config["ClassName"]).value)
                self.classList[__i].setdefault("WeekStatus", 0)
                # 是否需要移除教室名中的描述部分
                if self.note_config["isRemoveClassroomDescription"] == 0 or self.table.cell(i, self.config["Classroom"]).value.find('-') == -1:
                    self.classList[__i].setdefault(
                        "Classroom", self.table.cell(i, self.config["Classroom"]).value)
                else:
                    classroomWork: str = self.table.cell(
                        i, self.config["Classroom"]).value
                    classroomWork = classroomWork.split('-')[1]
                    self.classList[__i].setdefault("Classroom", classroomWork)

                if self.config["isClassSerialEnabled"][0]:
                    try:
                        self.classList[__i].setdefault("ClassSerial",
                                                       str(int(self.table.cell(
                                                           i, self.config["isClassSerialEnabled"][1]).value)))
                    except ValueError:
                        self.classList[__i].setdefault("ClassSerial",
                                                       str(self.table.cell(i, self.config["isClassSerialEnabled"][1]).value))
                if self.config["isClassTeacherEnabled"][0]:
                    self.classList[__i].setdefault("Teacher",
                                                   self.table.cell(i, self.config["isClassTeacherEnabled"][1]).value)
            i += 1

    def write_data(self):
        if os.path.exists("conf_classInfo.json"):
            print("已存在 JSON 文件, 自动覆盖")
            os.remove("conf_classInfo.json")
        filename = "conf_classInfo.json"
        with open(filename, 'w', encoding='UTF-8') as json_file:
            json_str = json.dumps(self.classList, ensure_ascii=False, indent=4)
            json_file.write(json_str)
            json_file.close()

    def main(self):
        if self.confirm_conf():
            sys.exit()
        self.load_data()
        self.write_data()
        print("Excel 文件读取成功. ")


if __name__ == "__main__":
    p = ExcelReader()
    p.main()
    print(p.classList)
