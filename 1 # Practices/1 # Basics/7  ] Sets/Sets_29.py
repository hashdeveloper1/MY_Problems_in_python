# float()
# int()
# ord()
# chr()
# str()
# set()
# list()
# tuple()
# ==============================
# st.clear()
# print(c | a | b)
# print(a.union(b, c))
# a.add(3)
# aa = a.copy()
# a.remove(1)
# a.discard(2)
# print(aa.pop())
# ss1.update(ss2)
# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(a.issuperset(b))  # True
# print(a.issubset(b))  # False
# print(a.isdisjoint(b))  # False
# ===============================
print("="*10)
a = {1, 2, 3}
b = {1, 2}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
print(a.issuperset(c))  # False
print("="*10)
# ===============================
print("="*10)
a = {1, 2, 3}
b = {1, 2}
c = {1, 2, 3, 4, 5}
print(a.issubset(b))  # False
print(a.issubset(c))  # True
print("="*10)
# ===============================
print("="*10)
a = {1, 2, 3}
b = {11, 22}
c = {1, 2, 3, 4, 5}
print(a.isdisjoint(b))  # False
print(a.isdisjoint(c))  # True
print("="*10)
# ===============================
