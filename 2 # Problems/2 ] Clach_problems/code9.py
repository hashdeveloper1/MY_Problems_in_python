
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

c = 1

for i in range(n):
    l = []
    for j in range(i+1):
        l.append(c)
        c += 1
    s = ''
    for k in range(len(l)):
        if k < len(l)-1:
           s += str(l[k]) + ' '
        else:
           s += str(l[k])
    print(s)

