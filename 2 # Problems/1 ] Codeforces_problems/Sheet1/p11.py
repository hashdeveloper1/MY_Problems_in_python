n = int(input())
for i in range(n):
    s = input().split()
    s1, s2 = s[0], s[1]
    rs = ''
    for j in range(min(len(s1), len(s2))):
        rs += s1[j] + s2[j]
    if len(s1) < len(s2):
        rs += s2[len(s1):]
    elif len(s1) > len(s2):
        rs += s1[len(s2):]
    print(rs)

