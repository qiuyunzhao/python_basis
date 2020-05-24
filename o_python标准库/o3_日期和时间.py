from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)
print(type(dt))  # <class 'datetime.datetime'>

print(dt)  # 2011-10-29 20:30:21
print(dt.year)  # 2011
print(dt.month)  # 10
print(dt.day)  # 29
print(dt.hour)  # 20
print(dt.minute)  # 30
print(dt.second)  # 21

print(dt.date())  # 2011-10-29
print(type(dt.date()))  # <class 'datetime.date'>
print(dt.time())  # 20:30:21
print(type(dt.time()))  # <class 'datetime.time'>

print("================== 将 datetime 格式化为字符串 =====================")
print(dt.strftime('%m/%d/%Y %H:%M'))  # 10/29/2011 20:30

print("================== 将字符串转换成 datetime 对象 ===================")
dt1 = datetime.strptime('20091031', '%Y%m%d')
print(dt1)  # 2009-10-31 00:00:00

dt2 = datetime.strptime('20091031 10:20:50', '%Y%m%d %H:%M:%S')
print(dt2)  # 2009-10-31 10:20:50

# 替换日期时间中的某部分
dt3 = dt2.replace(minute=0, second=0)
print(dt3)  # 2009-10-31 10:00:00

print("================== 两个 datetime 对象求差 ===================")
delta1 = dt2 - dt3
print(type(delta1))  # <class 'datetime.timedelta'>
print(delta1)  # 0:20:50

delta2 = dt3 - dt2
print(delta2)  # -1 day, 23:39:10

print(dt3 + delta1 == dt2)  # True
