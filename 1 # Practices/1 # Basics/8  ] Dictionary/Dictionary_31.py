# ===============================
#     -- Dictionary Methods --
# ===============================
# dic.clear()
# dic.update()
# dic.copy()
# dic.keys()
# dic.values()
# ===============================
print("="*10)
dic = {
    'name': 'hashem',
    'age': 24
}
print(dic)
dic.clear()
print(dic)
print("="*10)
# ===============================
print("="*10)
dic = {
    'name': 'hashem',
    'age': 24
}
print(dic)
dic.update({'salary': 50000})
print(dic)
dic['Gender'] = 'Male'
print(dic)
print("="*10)
# ===============================
print("="*10)
dic = {
    'name': 'hashem',
    'age': 24
}
b = dic.copy()
print(b)
print(dic)
dic['skills'] = ['HTML', 'CSS', 'JS', 'Python', 'C++', 'XML', 'Odoo', 'OOP', 'Data structure']
print(dic)
print(b)
print("="*10)
# ===============================
print("="*10)
dic = {
    'name': 'hashem',
    'age': 24
}
print(dic.keys())
print(dic.values())
print("="*10)
# ===============================

