#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
a, b = input(), input()
a, b = a[1:], b[1:]
print(f"RGB({int((int(a[0:2], 16)/2)+(int(b[0:2], 16)/2))} , {int((int(a[2:4], 16)/2)+(int(b[2:4], 16)/2))} , {int((int(a[4:6], 16)/2)+(int(b[4:6], 16)/2))})")