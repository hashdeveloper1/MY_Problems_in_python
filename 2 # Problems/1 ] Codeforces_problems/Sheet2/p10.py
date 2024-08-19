s = input()
if len(s) == 1:
    print(s)
else:
    m = 'z'
    l = []
    for i in range(1, len(s)):
        s1 = ''.join(sorted(s[:i]))
        s2 = ''.join(sorted(s[i:]))
        l.append(s1+s2)
    l = sorted(l)
    print(l[0])