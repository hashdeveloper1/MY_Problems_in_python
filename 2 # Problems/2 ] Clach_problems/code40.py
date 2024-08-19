#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import math
n1 = int(input())
n2 = int(input())
print(f"{n1//math.gcd(n1, n2)}/{n2//math.gcd(n1, n2)}")
