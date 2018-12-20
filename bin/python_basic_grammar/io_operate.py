import operator as op
import os

print("Are you ready to pratice your file operate in python?:")
answer = input("your answer:")
print(answer)
print(id(answer))
yes = "yes"
print(id(yes))
if not op.eq(answer, yes):
    print("exit!")
else:
    print(os.getcwd())
    #======================reading
    f1 = open("config/log1.txt", "r") # just read! Initial position is the beginning!
    print(f1.readlines())

    #======================writing
    f2 = open("config/log2.txt", "w") # write and also truncate file!
    content = "Test for open(\"config/log2.txt\", \"w\")\nwrite and also truncate file?"
    f2.close()
    f2 = open("config/log2.txt", "a") # write and don't truncate the file,write from the beginning of the file!
    f2.writelines("write and don't truncate the file.\nwrite from the beginning of the file!\n")
    f2.writelines(content)
    #======================reading and writing
    f3 = open("config/log3.txt", "w+")  # read and write and truncate the file
    # print(f3.readlines()) # nothing is here
    f3.writelines("aaaa/gggg/n")
    f3.close()
    f3 = open("config/log3.txt", "r+")
    f3.writelines("read and write and don't truncate \nbut from beginning!") # read and write and don't truncate but from beginning!
    f3.write("end!")
    f3.close()
    f3 = open("config/log3.txt", "a+")
    f3.writelines("read and write and don't truncate\n  initial position end!")
    
    f1.close()
    f2.close()
    f3.close()
