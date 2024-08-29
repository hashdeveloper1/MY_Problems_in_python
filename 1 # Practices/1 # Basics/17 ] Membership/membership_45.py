################################################
#           -- Membership Operator --
################################################
# IN String
name = "Hashem Ahmed Mahmoud"
ser = input()
if ser in name:
    print('YES')
else:
    print("NO_NOT_Found!!!")

# IN List
friends = ['Ali', 'Abdo', 'Hashem', 'Yasser']
print('Ali' in friends)
print('Abdo2' in friends)
print('Yasser' not in friends)
