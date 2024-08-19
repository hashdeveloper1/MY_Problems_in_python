##################################################
#                list method                     #
##################################################
# 01 ] list.append()
# 02 ] list.extend()
# 03 ] list.remove()
# 04 ] list.sort(reverse=True)
# 05 ] list.reverse()
# 06 ] list.clear()
# 07 ] list.count(value)
# 08 ] list.index(value)
# 09 ] list.insert(index,value)
# 10 ] list.pop(index)
##################################################
lis = ['A', 'B', 'C', 'D']
lis.clear()
print(lis)
# ------------------------------
lis = [1, 2, 3, 4, 5]
a = lis.copy()
lis.append(lis[-1]+1)
print(a)
print(lis)
# ------------------------------
lis = [1, 2, 3, 4, 5, 6, 1, 8, 1, 2]
print(lis.count(1))
print(lis.count(2))
print(lis.count(10))
# ------------------------------
lis = [1, 2, 3, 4, 5, 6, 1, 8, 1, 2]
if lis.index(2):
    print("Yes")
else:
    print("Not")
# ------------------------------
lis = [1, 2, 3, 4, 55, 6, 1, 8, 1, 2]
print(type(lis))
str_list = [str(i) for i in lis]
# for i in range(len(lis)):
#     lis[i] = str(lis[i])
print(type(str_list ))
print(str_list)
# lis = map(str, lis)
# s = ''.join(lis)
# print(s+'2')
# ------------------------------
lis = [1, 2, 3, 4, 55, 6, 1, 8, 1, 2]
lis.insert(7,"Hashem")
print(lis)
lis.insert(-1, "Hashem")
print(lis)
# ------------------------------
lis = [1, 2, 3, 4, 55, 6, 1, 8, 1, 2]
print(lis)
print(lis.pop(0))
print(lis.pop(1))
print(lis.pop(2))
print(lis.pop(3))
print(lis.pop(4))
print(lis)
# ------------------------------
