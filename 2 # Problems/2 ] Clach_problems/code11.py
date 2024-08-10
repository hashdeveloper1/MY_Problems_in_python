s = input()
n = int(input())
l = []
tem = ''
c = 0
for i in range(len(s)):
    c += 1
    if c <= n:
        tem += s[i]
    else:
        l.append(tem)
        tem = ''
        c = 1
        tem += s[i]


if c >= 1:
    l.append(tem)
s = ''
for i in range(len(l)):
    if i < len(l)-1:
        s += l[i]
        s += '-'
    else:
        s += l[i]

print(s)
