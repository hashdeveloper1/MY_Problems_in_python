t1 = ('Hashem',)
t2 = "Hashem",
print(t1)
print(t2)

print(type(t1))
print(type(t2))

print(len(t1))
print(len(t2))

c = t1 + t2
b = t1 + ("Ahmed", "Mahmoud")
print(c)
print(b)

a = ("1", "2")
b = [1,2]
print(a * 6)
print(b * 6)

a = ('A', 'B', 4, 'C')
x, y, _, z = a
print(x)
print(y)
print(z)
