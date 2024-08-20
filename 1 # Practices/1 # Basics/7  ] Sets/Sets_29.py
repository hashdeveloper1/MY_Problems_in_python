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
# ===============================
print("="*10)
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1)
print(s1.difference(s2))
print(s1)
print("="*10)
# ===============================
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1)
s1.difference_update(s2)
print(s1)
print("="*10)
# ===============================
print("="*10)
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1)
print(s1.intersection(s2))
print(s1)
print("="*10)
# ===============================
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1)
s1.intersection_update(s2)
print(s1)
print("="*10)
# ===============================
print("="*10)
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1)
print(s1.symmetric_difference(s2))
print(s1)
print("="*10)
# ===============================
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1)
s1.symmetric_difference_update(s2)
print(s1)
print("="*10)
# ===============================
