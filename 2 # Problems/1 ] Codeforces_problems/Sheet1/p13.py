n = int(input())
s = input()
l = []
ss = ''
m = 0
for i in range(len(s)):
    if i == 0:
        ss += s[i]
    else:
        if s[i] != s[i-1]:
            ss += s[i]
    if i == len(s)-1:
        l.append(ss)

for i in l:
    m = max(m, len(i))
print(m)
