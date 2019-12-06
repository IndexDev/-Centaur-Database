#Time&1
import #导入 time #时间‘模块’
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #格式化时间格式
"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59
"""
#Time&2
cal = calendar.month(2019, 12)#年月份
 #对应了import calendar
print ("以下输出2019年12月份的日历:") #变量字符串
print (cal)
