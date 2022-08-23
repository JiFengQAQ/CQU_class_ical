from calendar import weekday
from os import times


def classTimeTranslate(timeStr: str):
    classList = list()
    weekDayRef = dict()
    weekDayRef["一"] = 1
    weekDayRef["二"] = 2
    weekDayRef["三"] = 3
    weekDayRef["四"] = 4
    weekDayRef["五"] = 5
    weekDayRef["六"] = 6
    weekDayRef["日"] = 7
    # 周次处理(多个区间拆分为多个)
    while True:
        if timeStr.find(',') != -1:  # 如果周次有多个范围
            (weekRange, timeStr) = timeStr.split(',', 1)
            if weekRange.find('-') != -1:  # 如果周次是区间
                (startWeek, endWeek) = weekRange.split('-')
            else:
                startWeek = endWeek = weekRange
            classList.append(dict())
            classList[-1].setdefault("StartWeek", int(startWeek))
            classList[-1].setdefault("EndWeek", int(endWeek))
            classList[-1].setdefault("WholeWeek", False)
        else:
            (weekRange, timeStr) = timeStr.split('周', 1)
            if weekRange.find('-') != -1:  # 如果周次是区间
                (startWeek, endWeek) = weekRange.split('-')
            else:
                startWeek = endWeek = weekRange
            classList.append(dict())
            classList[-1].setdefault("StartWeek", int(startWeek))
            classList[-1].setdefault("EndWeek", int(endWeek))
            classList[-1].setdefault("WholeWeek", False)
            break  # 结束周次处理

    # 处理“占周不占时间”
    if timeStr.find('节') == -1:
        for i in range(len(classList)):
            classList[i]["WholeWeek"] = True
        return classList

    # 星期几
    weekDay = timeStr[2]
    timeStr = timeStr[3:]
    for i in range(len(classList)):
        classList[i].setdefault("Weekday", weekDayRef[weekDay])
    # 节次
    classTime = timeStr[:-1]
    if classTime.find('-') != -1:  # 如果节次是区间
        (classStartTime, classEndTime) = classTime.split('-')
    else:
        classStartTime = classEndTime = classTime
    for i in range(len(classList)):
        classList[i].setdefault("ClassStartTimeId", int(classStartTime))
        classList[i].setdefault("ClassEndTimeId", int(classEndTime))
    return classList
