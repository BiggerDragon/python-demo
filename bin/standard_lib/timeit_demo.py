from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())

print(Timer("for x in range(100):\n    a=a+x;", "a=0;").timeit())

print(Timer("for x in range(100):    a=a+x;", "a=0;").timeit())

print(Timer("while i < 100:    a=a+i;i=i+1;", "i=0;a=0;").timeit())



