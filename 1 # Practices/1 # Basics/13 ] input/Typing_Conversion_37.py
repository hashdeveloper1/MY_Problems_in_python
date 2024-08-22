# ===============================
#    -- Typing Conversion --
# ===============================
# str()
# int()
# tuple()
# list()
# set()
# dict()
# ===============================
n = 10
print((str(n) + '-')*2)
# ----------------------
s = "Hashem"
ll = [1, 2, 3, 4, 5]
st = {'A', 'B', 'C'}
dic = {'A': 1, 'B': 2}
print(tuple(s))
print(tuple(ll))
print(tuple(st))
print(tuple(dic))
print('$'*50)
# ----------------------
s = "Hashem"
tp = (1, 2, 3, 4, 5)
st = {'A', 'B', 'C'}
dic = {'A': 1, 'B': 2}
print(list(s))
print(list(tp))
print(list(st))
print(list(dic))
print('$'*50)
# ----------------------
s = "Hashem"
tp = (1, 2, 3, 4, 5)
ll = ['A', 'B', 'C']
dic = {'A': 1, 'B': 2}
print(set(s))
print(set(tp))
print(set(ll))
print(set(dic))
print('$'*50)
# ----------------------
tp = ((1, '2'), (2, 'D'))
ll = [['A', 1], ['B', 2]]
print(dict(tp))
print(dict(ll))
# ----------------------
