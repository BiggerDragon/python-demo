import time
import datetime
import timeit

print(time)
print(datetime)
print(timeit)

# 获取当前时间戳
print(time.time())

print("sleep 3s!")
time.sleep(3)
print(time.ctime())

# 获取时间tuple
print(time.localtime(time.time()), '=====', type(time.localtime(time.time())))
struct_time1 = time.localtime(time.time())
print('year=', struct_time1.tm_year)
print("month=", struct_time1.tm_mon)
print("mday=", struct_time1.tm_mday)
print("hour=", struct_time1.tm_hour)
print("min=", struct_time1.tm_min)
print("sec=", struct_time1.tm_sec)
print("wday=", struct_time1.tm_wday)
print("yday=", struct_time1.tm_yday)
print("isdst=", struct_time1.tm_isdst)

# 获取格式化时间
print(time.asctime(time.localtime(time.time())))

# 格式化日期
print(time.strftime('%y-%m-%d',  time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 将格式字符串转换成日期
str = "2018-11-22 22:11:12"
print(time.localtime(time.mktime(time.strptime(str, "%Y-%m-%d %H:%M:%S"))))

