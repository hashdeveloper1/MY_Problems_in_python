#  -- Hash Clash --
# o1 = "Strong palindrome"
# o2 = "Weak palindrome"
# o3 = "Not a palindrome"
#
# s = input()
# rs = s[::-1]
# if s == rs:
#     print(o1)
# else:
#     s2 = ''
#     for i in s:
#         if i.isalpha() and i.islower():
#            s2 += i
#
#     rs = s2[::-1]
#     if rs == s2 and s2 != '':
#         print(o2)
#     else:
#         print(o3)
 # ----------------------------------------------------------------------------------------- othor way

s = "ASDGdssldlww2133qsd"
# s = ''.join(c for c in s.lower() if c.isalpha())
s = ' '.join(c for c in s.lower() if c.isalpha())
# s = ''.join()
print(s)
####################################33


if s[::-1]==s:print('Strong palindrome');exit()

s=''.join(c for c in s.lower() if c.isalpha())

if s[::-1]==s:print('Weak palindrome');exit()
print('Not a palindrome')

