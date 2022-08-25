# CQU_class_ical
本工具基于[SunsetYe66](https://github.com/SunsetYe66)的[ClasstableToIcal](https://github.com/SunsetYe66/ClasstableToIcal), 可将重庆大学教务网生成的课表转化为ics日历, 方便大家快速查看和设置提醒, 无需借助任何第三方网络服务和app. 

## 使用说明

1.   先安装依赖: 

```shell
pip install uuid xlrd 
```

2.   将该项目克隆到本地: 

```shell
git clone https://github.com/JiFengQAQ/CQU_class_ical.git
```

或直接在网页上选择`Download ZIP`

3.   从[重庆大学教务管理系统-选课管理](https://my.cqu.edu.cn/enroll/Home)中下载整个学期Excel文件格式的课表

4.   将课表“另存为”到项目根目录, 并重命名、修改格式为`classInfo.xls`, 注意后缀名需要是`.xls`, 即`Excel 97-2004 工作簿`;

     您亦可选择复制全部条目到项目根目录的示例文件`simple_classInfo.xls`中, 并重命名为`classInfo.xls`

5.   执行 `main.py`, 先使用功能`2`, 再使用功能`3`: 

```shell
python main.py
# or
python3 main.py
```

测试环境: Python 3.7.9, macOS Monterey(12.4)

## 项目功能

-   导入重庆大学教务网的课表并制作为ics日历文件
-   支持不同周次、不同节次的自动识别、分割和合并
-   `占周不占时间`的课程暂<b><u>不</u></b>被支持, 程序会自动跳过
-   支持标记任课教师和课程班号(默认禁用, 因为可能会被部分系统误识别为电话号码)
-   可设置课前提醒(未经过测试)
-   支持创建单独的周号标记, 不再需要查校历或者慢慢数

## 进一步说明

### 示例课表文件

`simple_classInfo.xls`

就是按照`my.cqu.edu.cn`	下载的文件格式来的, 应该没啥问题.

记得只认`.xls`文件. 

### 具体行课时间表

`conf_classTime.json`	

就是按照学校时间设置的, 也可以自己对照着改. 

### 是否显示教师、是否显示课程班号

可在 `excel_reader.py` 的第23, 24行中更改每行的第一个数字来开启和关闭(`0`关闭, `1`开启) 

## To Do

-   添加对整周课程的支持
-   将教师、班号开关从代码中独立出来
-   能够删除上课教室中的描述性文字
-   优化命令行交互体验

## License

LGPLv3
