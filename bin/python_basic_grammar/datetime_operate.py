import datetime
import time as _time

print(datetime)

dt = datetime.datetime(2018, 12, 20)
print(dt)
print(type(dt))
print(dt.now())

# 将字符串解析城datetime
print(dt.strptime("2018-11-23", "%Y-%m-%d"), ' ', type(dt.strptime("2018-11-23", "%Y-%m-%d")))

# 格式化字符串日期
print(dt.strftime(str(dt)), ' ', type(dt.strftime(str(dt))))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.time())