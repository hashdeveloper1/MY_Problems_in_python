name = "Hashem"
country = "ASW"
student = True
course_name = "Python Course"
course_price = 100

if country == 'Egypt' or country == 'ASW':
    print(f'Hello {name} ....')
    if student:
        print(f"Because you from {country} Your course Price is : ${course_price-90}")
    else:
        print(f"Because you from {country} Your course Price is : ${course_price - 80}")
else:
    print(f'Hello {name} ....')
    print(f"Because you from {country} Your course Price is : ${course_price - 30}")