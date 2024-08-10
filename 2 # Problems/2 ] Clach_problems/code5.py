import sys
import math

l = int(input())
n = int(input())
c = 1
for i in range(n):
    s = ''
    for j in range(l):
        s += str(c)
        c += 1
    s = ','.join(s)
    s = s.ljust(len(s)+1, ']')
    s = s.rjust(len(s)+1, '[')
    print(s)

