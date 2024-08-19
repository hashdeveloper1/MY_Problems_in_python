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
n, k = [int(i) for i in input().split()]
l = []
if n > k:
    sum = 0
    while(True):
        if sum + k < n:
          sum += k
          l.append(k)
        else:
          l.append(n - sum)
          break
    s = ''
    for i in l:
        s += str(i) + ' '
    print(s[:-1])
else:
    print(n)