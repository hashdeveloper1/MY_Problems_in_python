# ===============================
#        -- Dictionary --
# ===============================

# ===============================
print("="*10)
user = {
    'name': 'Hashem',
    'age': 24,
    'salary': 24000,
    'skills': ['HTML', 'CSS', 'JS']
}
print(user)
print(user['name'])
print(user['age'])
print(user['skills'][2])
print(user.get('salary'))
print(user.keys())
print(user.values())
print("="*10)
# ===============================
print("="*10)
languages = {
    'one': {
        'name': 'python',
        'progress': '70%',
    },
    'tow': {
        'name': 'Odoo',
        'progress': '60%',
    },
    'three': {
        'name': 'postgresql',
        'progress': '20%',
    }
}
print(languages)
print(languages['one'])
print(languages['tow'])
print(languages['three'])
print("="*10)
# ===============================
print("="*10)

framwork1 = {
    'name': 'python',
    'progress': '70%',
}
framwork2 = {
    'name': 'Odoo',
    'progress': '60%',
}
framwork3 = {
    'name': 'postgresql',
    'progress': '20%',
}

Allframwork = {
    'one': framwork1,
    'tow': framwork2,
    'three': framwork3,
}
print(Allframwork)
print("="*10)
# ===============================
