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
print("full mathced" if mo is not None else "not full macthed")

mo =re.fullmatch(reg, "Happy coding!斗破苍穹,I will fight the sky broken!")
print("full matched" if mo is not None else "not full mathed!")




