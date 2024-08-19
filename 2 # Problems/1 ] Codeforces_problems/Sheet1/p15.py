s = input()
w = "EGYPTegypt"
w1 = "EGYPT"
w2 = "egypt"
d = {'E': 0}
for i in w:
    d[i] = 0
for i in s:
    if w.find(i) > -1:
        d[i] += 1
m = 1000000000
for i in range(5):
    if (d[w1[i]] + d[w2[i]]) > 0:
        m = min(m, (d[w1[i]] + d[w2[i]]))
    else:
       m = 0
       break
print(m)