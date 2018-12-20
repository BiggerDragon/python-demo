s1 = "yes"
s2 = str("yes")

print(s1 is s2)
print(s1.__eq__(s2))

import operator as op
print(op.eq(s1, s2))