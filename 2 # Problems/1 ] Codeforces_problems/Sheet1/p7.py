import math

ln = input().split()
n1 = float(ln[0])
n2 = float(ln[1])
print(f"floor {int(n1)} / {int(n2)} = {math.floor(n1/n2)}")
print(f"ceil {int(n1)} / {int(n2)} = {math.ceil(n1/n2)}")
sum = (n1/n2) - (n1//n2)
if sum >= 0.5:
    print(f"round {int(n1)} / {int(n2)} = {math.ceil(n1/n2)}")
else:
    print(f"round {int(n1)} / {int(n2)} = {round(n1 / n2)}")
