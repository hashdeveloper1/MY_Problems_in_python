#--------------------------------------------------------------------------------
# Problem 2 : B. Basic Data Types
# Solved by Hashem
#--------------------------------------------------------------------------------

str1 = input()
val = ""
for i in str1:
    if i != ' ':
        val = val + i
    else:
        print(val)
        val = ""
print(val)