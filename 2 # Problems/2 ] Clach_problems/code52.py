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
# c = eval(f"{c}{a}{b}")

import sys
import math

a, b = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    x, y, r = [int(j) for j in input().split()]
    p1 = (x+r,y)
    p1 = (x+r,y)

