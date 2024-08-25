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
s = input()
ss = ''
for i in range(ord('a'), ord('z')+1):
    if chr(i).isalpha():
       ss += chr(i)
d = dict.fromkeys(ss, 0)
s = s.lower()

for i in s:
    if i.isalpha():
       d[i] += 1
c=0
for i in d:
    if d[i] > 0:
        c += 1
if c == 26:
    print('true')
else:
    print('false')