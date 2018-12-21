# file wildcards
import glob as gb

m_list = gb.glob("*")
print(m_list)

pathname = "D:/VsCodeWorkspace"

m_list = gb.glob("**", recursive=True)
print(m_list)
g = gb.iglob("*")
for x in g:
    print(x)
