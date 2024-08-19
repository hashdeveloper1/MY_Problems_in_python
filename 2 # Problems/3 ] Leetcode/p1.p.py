n = int(input())
t = {0: [1], 1: [1, 1]}  # [1,2,1]
if n == 0:
    print(t[n])
elif n == 1:
    print(t[n])
else:
    for i in range(2, n+1):
        # print(i)
        l = []
        l.append(1)
        for j in range(i-1):
            l.append(t[i-1][j]+t[i-1][j+1])
        l.append(1)
        t[i] = l
print(t[n])