#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import sys
import math

s = input()
ss = ''
for i in range(len(s)):
    if s[i].isalpha() and s[i].isupper():
       ss += str(i) + ","


if len(ss) == 0:
    print("None")
else:
    print(ss[:-1])