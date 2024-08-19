s = input()
f = "hello"
l = ''
c = 0
for i in range(len(s)):
   if s[i] == f[c]:
       l += s[i]
       c += 1
   if c == 5:
       break

if c >= 5:
    print("YES")
else:
    print("NO")