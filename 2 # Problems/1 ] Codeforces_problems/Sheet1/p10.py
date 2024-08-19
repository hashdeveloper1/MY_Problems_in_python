s = input()
d = {}
for i in range(ord('a'), ord('z')+1):
    d[chr(i)] = 0
for i in s:
    d[i] += 1
for i in d:
    if d[i] > 0:
        print(f"{i} : {d[i]}")