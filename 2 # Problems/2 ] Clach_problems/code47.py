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
import sys
import math

n = int(input())
d = {'+': 0, '-': 0}
b1, b2 = [],[]
for i in range(n):
    charges = input()
    for i in charges:
        d[i] += 1
    if d['+'] + d['-'] == len(charges):
        b1.append(1)
    elif d['+'] == len(charges) or d['-'] == len(charges):
        b2.append(1)
    else:
        print("nonsense")
        exit()

if len(b1) == n:
    print("attracts")
else:
    print("repels")