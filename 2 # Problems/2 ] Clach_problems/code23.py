#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
from itertools import cycle
C = cycle([10,6,0,10,6,24])

while 1:
    print(next(C))

print(next(C))
# N=int(input())
# i=0
# while N>0:N-=next(C);i+=1
# print(i)