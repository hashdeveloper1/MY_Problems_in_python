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
n = int(input())
s = ''
c = 0
for i in range(n):
    line = input()
    s += line
d = s.count(' ')
re = int((d / len(s)) * 100)
if len(s) == 0 or s == ' ':
    print(f"0%")
elif d > 0:
    print(f"{(100 - re -1)}%")
else:
    print(f"{100}%")

