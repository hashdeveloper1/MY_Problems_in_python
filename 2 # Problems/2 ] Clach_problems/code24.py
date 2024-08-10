#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
n = int(input())
d = int(input())
h = int(input())

sd = (n * h) // 24
if sd > d:
    print("It is enough")
elif sd == d:
    print("Just enough")
else:
    print("Not enough")
