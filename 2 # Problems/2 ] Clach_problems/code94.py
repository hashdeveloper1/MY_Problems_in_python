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
n = int(input())
re = 1
m = 0
mi = 1000000
for i in range(n):
    a = int(input())
    m = max(a,m)
    mi = min(a,mi)
print(int(math.sqrt(m*mi)))