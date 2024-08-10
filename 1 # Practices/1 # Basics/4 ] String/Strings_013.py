
# s = ''
#
# for i in range(100001):
#     s = str(i)
#     print(s.zfill(5))

str1 = "              [0109840805802485048050395734958637063808406801] ارز 12 اونز نصف مصنع"
# print(str1)
# print(str1.strip())
# print(str1.rstrip())
# print(str1.lstrip())

print(str1)
print(str1.strip(" [0123456789] "))
# print(str1.rstrip())
# print(str1.lstrip())

str1 = "process Finished with exit code 0"
print(str1.strip())
print(str1.title())
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
str1 = "12"
print(str1.zfill(5))
for i in range(5):
    left_padding = ('{:%>5}'.format(str1))
    print(left_padding)

