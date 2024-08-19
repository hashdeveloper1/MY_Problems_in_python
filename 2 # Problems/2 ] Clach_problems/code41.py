#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
s = input()
s = sorted(s)
ss = s[0]
for i in range(1,len(s)):
    ok = 1
    if s[i] == s[i-1]:
        ss += s[i]
    else:
        print(ss)
        ss = s[i]

print(ss)
# import sys
# import math
# from collections import defaultdict
#
# # Create a defaultdict with a default value of 0
# dic = defaultdict(int)
# s=input()
# s=sorted(s)
# for i in s:
#     dic[i]+=1
# for i in dic:
#     print(f'{i*dic[i]}')