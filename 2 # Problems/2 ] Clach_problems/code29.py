#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
al = 'AaEeOoIiUu'
s = input()
ss = ''
for i in s:
    if al.find(i) > -1:
       ss += i + 'p' + i
    else:
        ss += i
print(ss)