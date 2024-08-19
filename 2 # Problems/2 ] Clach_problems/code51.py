#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
# from collections import defaultdict
# # Create a defaultdict with a default value of 0
# dic = defaultdict(int)
# print(sum(ord(i)if ord(i)%2==1else 0 for i in input()))
import sys
import math

t = input().split()
num = t[::2]
op = t[1::2]
re = 0
for i in range(len(op)):
    if op[i] == '&':
       re = (int(num[i]) and int(num[i+1]))
       num[i+1] = str(re)
    else:
       re = (int(num[i]) or int(num[i + 1]))
       num[i + 1] = str(re)

print(re,len(op))


t = input().split()
c=int(t.pop(0))
for a,b in zip(t[::2], t[1::2]):
    c=eval(f"{c}{a}{b}")
print(c, len(t)//2)