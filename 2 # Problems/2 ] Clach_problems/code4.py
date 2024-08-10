s = "  [435808129753421]  Hashem Ahmed     [435808129753421]   "
str1 = "              [0109840805802485048050395734958637063808406801] ارز 12 اونز نصف مصنع"
s = str1
s = s.replace('[', '')
s = s.replace(']', '')
for i in range(10): s = s.replace(str(i), '')
s = s.strip(' ')
print(s)
