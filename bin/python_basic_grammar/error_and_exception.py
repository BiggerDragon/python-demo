# 语法错误和异常
try:
    num  = int(input("enter a number:"))
except ValueError:
    print("Please enter a number!")

import sys
import os

try:
    f = open("config/log1.txt")
    lines = f.readlines()
    num = int(input("Enter a number:"))
except OSError:
    print("file not exists")
except ValueError:
    print("please enter a number")
except:
    print("System unknow error!")
    raise


# 自定义异常
class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)

try:
    raise MyError("This is my Error")
except MyError as e:
    print(e.msg)
finally:
    print("Goodbye!")


