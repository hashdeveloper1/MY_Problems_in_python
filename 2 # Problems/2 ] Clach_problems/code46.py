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

beginner = input()
n = int(input())
r = int(input())
sum = 0
for i in input().split():
    m = int(i)
    sum += m
if sum < n:
    print("Nobody")
else:
    if r % 2 == 0:
       print(beginner)
    else:
        if beginner == 'Bob':
            print("Alice")
        else:
            print("Bob")import sys
import math

beginner = input()
n = int(input())
r = int(input())
sum = 0
for i in input().split():
    m = int(i)
    sum += m
if sum < n:
    print("Nobody")
else:
    if r % 2 == 0:
       print(beginner)
    else:
        if beginner == 'Bob':
            print("Alice")
        else:
            print("Bob")