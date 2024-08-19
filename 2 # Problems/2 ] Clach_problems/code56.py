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

d1, c1 = [int(i) for i in input().split()]
d2, c2 = [int(i) for i in input().split()]
re = int(input())
s = ''

for i in range(re):
    ss = str(d1+i) * c1 + str(d2+i) * c2
    s += ss
    print(i)
print(s)

