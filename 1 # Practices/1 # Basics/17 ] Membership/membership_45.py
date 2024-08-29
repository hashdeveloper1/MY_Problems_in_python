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
print(50 * '#')
# IN List
friends = ['Ali', 'Abdo', 'Hashem', 'Yasser']
print('Ali' in friends)
print('Abdo2' in friends)
print('Yasser' not in friends)
print(50 * '#')

countries_zone_1 = ['Egypt', 'KSA']
discount_zone_1 = 50
countries_zone_2 = ['Elsodan', 'Nijeraa']
discount_zone_2 = 80
my_country = input()
if my_country in countries_zone_1:
    print(f"Your discount is ${100 - discount_zone_1}")
elif my_country in countries_zone_2:
    print(f"Your discount is ${100 - discount_zone_2}")
else:
    print("Your Country is not Found in Countries List")
