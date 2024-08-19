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
d = {' ':0}

s = input()
for i in s:
    d[i] = 0
sord = 0
for i in s:
    d[i] += 1
for i in s:
    if i != ' ':
        if d[i]>0 and i.isalnum():
           sord += ord(i)
           print(i)
           d[i] = 0
print(f"{sord%8}/10")