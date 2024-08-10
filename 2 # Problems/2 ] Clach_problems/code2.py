
n = int(input())
s = ''
for i in range(n):
    s = ''
    for j in range(n - i):
        s += str(j+1)
    s = s.rjust(n, '+')
    print((s))

