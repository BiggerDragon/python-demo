import pickle

obj = {1:"one", 2: "two", 3: "three"}

obj_output = open("config/obj.pkl", "wb") # 打开文件
pickle.dump(obj, obj_output) # 将对象写入文件
obj_output.close()

f = open("config/obj.pkl", "rb") # 打开文件
obj2 = pickle.load(f) # 将文件读取到内存中
print(obj2)
f.close()

