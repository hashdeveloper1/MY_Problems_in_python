s = input().split()
ss = ''
for i in range(len(s)):
    if i != len(s)-1:
       ss += s[i][::-1] + ' '
    else:
       ss += s[i][::-1]
print(ss)
