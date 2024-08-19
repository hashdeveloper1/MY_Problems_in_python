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
# s = input()
# s = s.replace(' ','')
# s = s.replace('|','')
# ss = ''
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         ss += s[i]+s[i+1]
#     i += 1
# print(ss)


import sys
import math
import re

o = input()

a = re.findall('|^^',orbitals)
print(a)
print(' '.join(a) if a else 'Correct')