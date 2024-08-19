#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
ids = input()
s = input()
d ={ids[0]: 0}
for i in range(1, len(ids)):
    d[ids[i]] = i
ss = ''

for i in range(1, len(s)+1):
    ss += s[d[str(i)]]
print(ss)
