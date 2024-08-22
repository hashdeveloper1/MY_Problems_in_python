# ===============================
#     -- Dictionary Methods --
# ===============================
# dic.clear()
# dic.update()
# dic.copy()
# dic.keys()
# dic.values()
# dic = dict.fromkeys(s, 0) string or list or tuple  to dict
# dic.setdefault('name', 'Ahmed') print(dic.setdefault('age')) print(dic.setdefault('age', 24))
# dic.popitem()
# ===============================
print("="*10)
dic ={
    'name': 'Hashem'
}
print(dic)
print(dic.setdefault('name', 'Ahmed'))
print(dic.setdefault('age'))
print(dic)
print("="*10)
# ===============================
print("="*10)
dic = {
    'name': 'Hashem'
}
dic.update({'age': 24})
print(dic.popitem())
print("="*10)
# ===============================
print("="*10)
dic = {
    'name': 'Hashem'
}
items = dic.items()
print(items)
dic.update({'salary': 22000})
print(items)
for i in items:
    print(i[0], " : ", i[1])
print("="*10)
# ===============================
print("="*10)
s = input()
s = sorted(s)
dic = dict.fromkeys(s, 0)
for i in s:
    dic[i] += 1
for i in dic:
    print(i, ' : ', dic[i])
print("="*10)
# ===============================