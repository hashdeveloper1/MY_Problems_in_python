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
# print(sm(ord(i)if ord(i)%2==1else 0 for i in input()))
# c = eval(f"{c}{a}{b}")
import sys
import math

s = input()
ss = ''
for i in s:
    if i == '.':
        ss += '1'
    elif i == '-':
        ss+='0'
    else:
        ss+=i
ss = ss.split()
su = 0
for i in ss:
    su += int(i, 2)
    print(i, int(i, 2))
print(su)
