##################################################
#                list method                     #
##################################################
# 1 ] list.append()
# 2 ] list.extend()
# 3 ] list.remove()
# 4 ] list.sort(reverse=True)
# 5 ] list.reverse()
my_list = ["Hashem", "Ahmed"]
old_list = ["El Mahdi", "Ebrahim"]
my_list.append("Mahmoud")
my_list.append(old_list)
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3][1][0])
a = [1, 2, 3]
b = ['a', 'n', 'c']
a += b
print(a)
a.extend(b)
print(a)

b = ['a', 'n', 'c', 'a']
b.remove('a')
print(b)

a = [1, 3, 2, 7, 4, -1, -10, -40]
a.sort()
print(a)

n = [5, 4, 10, 2, 1]
n.sort(reverse=True)
print(n)
n = ['Z', 'B', 'C', 'A']
n.sort()
print(n)


n = ['A', 'B', 'C']
n.reverse()
print(n)

