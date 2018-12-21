import re
#         match     Match a regular expression pattern to the beginning of a string.
#         fullmatch Match a regular expression pattern to all of a string.
#         search    Search a string for the presence of a pattern.
#         sub       Substitute occurrences of a pattern found in a string.
#         subn      Same as sub, but also return the number of substitutions made.
#         split     Split a string by the occurrences of a pattern.
#         findall   Find all occurrences of a pattern in a string.
#         finditer  Return an iterator yielding a Match object for each match.
#         compile   Compile a pattern into a Pattern object.
#         purge     Clear the regular expression cache.
#         escape    Backslash all non-alphanumerics in a string.

mo = re.match("powerful", "powerful")
print(mo)
print(mo.group())
reg = "Happy coding!斗破苍穹"
mo = re.match(reg, "Happy coding!斗破苍穹,I will fight the sky broken!")
if mo is not None:
    print(mo.group())

mo = re.fullmatch(reg, "Happy coding!斗破苍穹")
print("full mathced" if mo is not None else "not full matched")

mo =re.fullmatch(reg, "Happy coding!斗破苍穹,I will fight the sky broken!")
print("full matched" if mo is not None else "not full matched!")

so = re.search("engine", "Car engine is the heart of it")
print(so.group() if so is not None else "not searched!")

s = re.sub("name", "大龙", "name is name")
print(s)

sn = re.subn("name", "small dragon", "name is name")
print(sn)

split_result = re.split(",", "Dog,Cat,Pig,Dragon,Duck")
print(split_result)

find_result = re.findall("Alien", "Alien comes from M78, Alien has no brain! alien eats people!")
print(type(find_result), find_result)

find_iter_result = re.finditer("Alien", "Alien comes from M78, Alien has no brain! alien eats people!", flags=0)
print(type(find_iter_result))
for x in find_iter_result:
    print(x.group())


reg = "[a-zA-z0-9_]"
print(type(reg))
print(type(re.compile(reg)))
re.purge()










