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
c1 = 0
c2 = 0
while True:
  if n == 1:
      break
  if n % 2 == 0:
      n = n//2
      c1 += 1
  else:
      n = (3*n)+1
      c2 += 1
print(c1)
print(c2)