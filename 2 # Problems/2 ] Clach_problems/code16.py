n = int(input())
s = 0
for i in range(n):
    earning, probability = [float(j) for j in input().split()]
    s += earning * probability

print("%.2f" %(s))
