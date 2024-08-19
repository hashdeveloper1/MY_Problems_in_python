#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char

s = input().split()
s1 = s[0]
s2 = s[1]
d1 = {}
d2 = {}
if len(s1) == len(s2):
    for i in range(len(s1)):
        d1[s1[i]] = 0
        d2[s2[i]] = 0
    for i in range(len(s1)):
        d1[s1[i]] += 1
        d2[s2[i]] += 1
    if d1 == d2:
        print("1")
    else:
        print("0")
else:
    print("0")