from collections import Counter

a=input()
b=input()
if len(a)!=len(b):
    print('NO')
c = Counter(a)
d = Counter (b)
if c==d:
    print('YES')