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

st = {'1', '2'}
print(type(st))
st.clear()
print(type(st))
a = {1, 2, 3}
b = {'one', 'tow', 'three'}
c = {11, 22, 33}
print(c | a | b)
print(a.union(b, c))
a = {1, 2}
a.add(3)
aa = a.copy()
# print(aa)
# # a.remove(5)
# # a.remove(1)
# a.discard(2)
# a.discard(7)
print(aa)
print(aa.pop())
print(aa)
ss1 = {1, 2, 3}
ss2 = {1, 2, 3, 4, 5}
ss1.update(ss2)