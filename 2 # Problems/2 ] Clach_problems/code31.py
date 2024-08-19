#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import sys
import math

n = int(input())
s = input().split()
print(s)
ok = 1
for i in range(len(s)-2):
     print(s[i])
     if (int(s[i]) + int(s[i+1])) != int(s[i+2]):
         ok = 0
         break

if ok:
    print(int(s[-1])+int(s[-2]))
else:
    print("Invalid")




