import math
#定义万年历函数
def calendar(year,month):
	#total_days记录输入年份的上一年到时间戳1900年的总天数；year_days记录输入月的一号是输入年的第几天；sum_days 是从1900年一月开始到输入月共有多少天。
    sum_days = 0
    total_days = 0
    year_days = 0
    days = 0
    遍历1900年到输入年的前一年，计算天数。其中闰年加366天，非闰年加365天。即total_days
    for i in range(year - 1,1899,-1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            total_days += 366
        else:
            total_days += 365
     #遍历月份，计算输入年一月一号到输入月前面一个月的最后一天共有几天，即year_days，其中			    #二月还的判断次年是否闰年
    for j in range(month - 1,0,-1):
        if j in [1,3,5,7,8,10,12]:
            year_days += 31
        elif j in [4,6,9,11]:
            year_days += 30
        else:
            if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
                year_days += 29
            else:
                year_days += 28
     #计算出总天数sum_days
    sum_days = total_days + year_days
    #1900年一月一号是星期一，计算出总天数除以7的余数，该余数加1即是输入月的1号对应的星期#数
    week_day = sum_days % 7
    #判断输入月的天数
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    else:
        if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
            days = 29
        else:
            days = 28
     #根据天数和上面求出的余数判断该月最多能输入几行（按日历格式，每行七天），调用math模#块中的cell方法（向上取整）
    row = math.ceil((week_day + days) / 7)
    #格式化的输出周一到周天（格式化的对其，需要慢慢来）
    print("周一"," 周二"," 周三"," 周四"," 周五"," 周六"," 周天")
	#第一行中非输入月日期对应的天数 用空格顶替
    for _ in range(week_day,0,-1):
        s = " "
        print(" %-5s" % s,end="")
     #第一行中剩余的天数的输出，p是该行需要输出输入月日期的天数
    for p in range(1,8-week_day):
        if p == 7 - week_day:
            print(" %-5d" % p)
        #如果到周末，输出换行
        else:
            print(" %-5d" % p,end="")
     #输出从第二行开始的输入月剩余的天数
    for q in range(8 - week_day,days + 1):
        if (q + week_day) % 7 == 0:
            print(" %-5d" % q)
        else:
            print(" %-5d" % q, end="")
#输入年，输入月
year = int(input("输入年："))
month = int(input("输入月："))
#调用万年历函数计算
calendar(year,month
————————————————
版权声明：本文为CSDN博主「Mr   Dou」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/MrDoulei/article/details/99766568
