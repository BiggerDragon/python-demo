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
