from urllib.request import urlopen

result = urlopen("http://baidu.com")
print(result)
# print(help(type(result)))
from http.client import HTTPResponse
# resp = HTTPResponse()
print(result.read())

result = urlopen("http://mm.263.com/")
print(result.read())

print(result.info())
print(result.getcode())
print(result.geturl())

