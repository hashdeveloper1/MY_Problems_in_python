def find_greater_divisor(n):
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

n = int(input())
x = n
l = [n]
while x != 1:
   x = find_greater_divisor(x)
   l.append(x)
l.pop()
l.sort()
if len(l):
    x = l[0]
for i in range(len(l)-1):
    x += (l[i+1] / l[i])
if len(l) == 0:
   print(0)
else:
   print(int(x))