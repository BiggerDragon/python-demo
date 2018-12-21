import zlib
# print(help(zlib))
s = b"Poem Libai drink a lot!"
print(len(s))
co = zlib.compress(s, level=9)
print(len(co))
print(co)
print(zlib.decompress(co))
