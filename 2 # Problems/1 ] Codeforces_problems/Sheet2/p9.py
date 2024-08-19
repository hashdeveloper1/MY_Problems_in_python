n = input()
s = map(int, input().split())
s = sorted(s)
ss = ''
c = 0
for i in s[::-1]:
    ss += str(i)
    if i == 0:
        c += 1
if c == len(s):
    print("0")
else:
    print(ss)