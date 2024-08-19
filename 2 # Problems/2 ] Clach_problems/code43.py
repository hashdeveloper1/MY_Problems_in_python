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
phone_number = input()
n = int(input())
l = []
ok = 0
for i in range(n):
    saved_number = input()
    if phone_number == saved_number:
        ok = 1
    l.append(saved_number)
s = ''
if ok:
    for i in phone_number:
        s += i
        c = 0
        for j in l:
            if j.startswith(s):
                c += 1
        if c == 1:
            print(s)
            break

else:
    print(phone_number)

# import sys
# import math
#
# # Phone auto-complete
#
# phone_number = input()
# n = int(input())
# l=[]
# for i in range(n):
#     l+=input(),
# if phone_number not in l:
#     print(phone_number)
#     sys.exit()
# for i in range(len(phone_number)+1):
#     s=phone_number[:i]
#     if sum(x.startswith(s) for x in l)==1:
#         print(s)
#         break
