#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char

s = input()
s = s[::-1]
s1 = ''
for i in s:
    if i.isalpha() or i == ' ':
      s1 += i
print(s1.upper())

