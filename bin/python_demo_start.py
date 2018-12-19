import re
print("Hello world github! you are good!")
print("I like python! I don't want to die!")
print("God bless me!")

reg_for_id_no = "[0-9]{17}[xX0-9]"

mo = re.match(reg_for_id_no, '411524199507037213')

print(mo.group(0))
