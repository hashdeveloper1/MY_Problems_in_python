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
sr = s[::-1]
for i in range(len(s)):
    print(s[i] + ' ' + sr[i])

for a, b in zip(s, s[::-1]):
    print(a, b)