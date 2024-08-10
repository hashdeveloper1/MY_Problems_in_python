#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
import sys
import math


f = {'50': ['0']}


def get_child(f, k):
    # print(k)
    lens = 0
    for i in f[k]:
        if i in f:
            lens += len(f[i]) + get_child(f, i)
    return lens


n = int(input())

for i in range(n):
    r = input().split()
    if r[0] in f:
        f[r[0]].append(r[1])
    else:
        nd = {r[0]: [r[1]]}
        f.update(nd)
p = input()
ok = 0
for i in f.keys():
    if i == p:
        print(get_child(f,p) + len(f[p]))
        print(f)
        ok = True
if not ok:
    print('0')
