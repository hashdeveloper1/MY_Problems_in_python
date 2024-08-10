# # hashcode 18
#
# n = int(input())  # The width and height of the board
# c = 0
# for i in range(n):
#     s = input()
#     for j in s:
#         if j.isnumeric():
#             c += 2**int(j)
#
# print(c)
# square = '0123456789ABCDEFG'
# print(int(square, 16))  # hixa_decimal from 0 to F

hexa_number = '02FF'
binary_number = '01100'
decimal_number_list = []
decimal_number_list.append(int(hexa_number, 16))  # convert 16 to decimal number
decimal_number_list.append(int(binary_number, 2)) # convert 2 to decimal number

print(decimal_number_list)  # Output [767, 12]
print((0 and 1))
print((0 and 0))
print((1 and 1))

s1 = '1010101010'
s2 = '1100110011'
re = ''
for i in range(len(s1)):
    re += str(int(s1[i]) and int(s2[i]))
print(re)
re = ''
for i in range(len(s1)):
    re += str(int(s1[i]) or int(s2[i]))
print(re)
re = ''
for i in range(len(s1)):
    re += str(int(not int(s1[i])))
print(re)

val = True
print(val)
print(int(val))
