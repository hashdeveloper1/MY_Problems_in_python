#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import sys
import math


n = int(input())
a = input().split()
m = 0
for i in a:
   n1 = abs(int(i))
   s = str(n1)
   s = s[::-1]
   m = max(m,int(s))
print(m)