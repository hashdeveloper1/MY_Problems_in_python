#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import sys
import math

l = input().split()
state = input().split()
ok = 0
if state[0] == '+':
    for i in range(len(l)):
        l[i] = str(int(l[i]) + (ord(state[1]) - 96))
    ok = 1
elif state[0] == '-':
    for i in range(len(l)):
        l[i] = str(int(l[i]) - (ord(state[1]) - 96))
    ok = 1
elif state[0] == '*':
    for i in range(len(l)):
        l[i] = str(int(l[i]) * (ord(state[1]) - 96))
    ok = 1
elif state[0] == '/':
    for i in range(len(l)):
        l[i] = str(int(int(l[i]) / (ord(state[1]) - 96)))
    ok = 1
else:
    print("Invalid")


s = ''
for i in l:
    if i != l[-1]:
       s += i + " "
    else:
        s += i
if ok:
   print(s)