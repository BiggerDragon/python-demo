import os

#===================using current uid and gid
b = os.access('config/log1.txt', os.W_OK) # can write?
print(b)
b = os.access('config/log1.txt', os.R_OK) # can read?
print(b)
b = os.access('config/log1.txt', os.X_OK) # can execute?
print(b)
b = os.access('config/log.txt', os.F_OK) # path exists?
print(b)

# =====================modify current working dir
print("current working dir is ", os.getcwd())
os.chdir("d:/VsCodeWorkspace")
print("current working dir is ", os.getcwd())

"""Reading authority of dir means the user can get the files list inside the dir.
Execute authority of dir means the user can cmd in this dir!
Deleting files from the dir must have the writing and executing authority at the
same time!
"""
# =====================modify path authority of file or dir
os.chdir("d:/VsCodeWorkspace/python-demo/")
import stat
os.chmod("config/log1.txt", stat.S_IREAD) # windows下设为只读
os.chmod("config/log1.txt", stat.S_IWRITE) # windows下取消只读


