import sys
import math

s= input().split()
s2 = 'AEIOUaeiou'
ss = ''
for i in s:
    c = 0
    for j in i:
        if s2.find(j) != -1:
            c += 1
    if i != i[-1]:
        ss += str(c) + ' '
    else:
        ss += str(c)
print(ss)