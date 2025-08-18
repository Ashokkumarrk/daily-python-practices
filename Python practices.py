s=54789
reversed_s = 0
for i in range(len(str(s))):
    reversed_s=reversed_s * 10 + s % 10
    s=s//10
print(reversed_s)

a=1056
reversed_s=0
while a>0:
    reversed_s=reversed_s*10 + a % 10
    a=a//10
print(reversed_s)

e=1088
reversed_s = 0
for i in range(len(str(e))):
    reversed_s =reversed_s * 10 + e % 10
    e=e//10
print(reversed_s)

d=1267
reversed_s = 0
while d>0:
    reversed_s = reversed_s * 10 + d % 10
    d=d//10
print(reversed_s)