# # -- Hash Clash --
def revers_str(s): return s[::-1]
# face = input()
# arm = input()
#
# s = arm + face
# for i in range(len(arm)):
#     if arm[len(arm) - i -1] == '<':
#         s += '>'
#     elif arm[len(arm) - i -1] == '>':
#         s += '<'
#     elif arm[len(arm) - i -1] == '/':
#         s += '\\'
#     elif arm[len(arm) - i -1] == '\\':
#         s += '/'
#     elif arm[len(arm) - i -1] == '[':
#         s += ']'
#     elif arm[len(arm) - i -1] == ']':
#         s += '['
#     elif arm[len(arm) - i -1] == '}':
#         s += '{'
#     elif arm[len(arm) - i -1] == '{':
#         s += '}'
#     else:
#         s += arm[len(arm) - i -1]
# print(s)
s = '12345 '
rs = revers_str(s)
print(rs)
print(s[::-1])
print(s[:-1])