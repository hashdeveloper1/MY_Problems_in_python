name = "Hashem"
country = "Egypt"
course_name = "Python Course"
course_price = 100

if country == 'Egypt':
    print(f'Hello {name} ....')
    print(f"Because you from {country} Your course Price is : ${course_price-80}")
elif country == 'ASW':
    print(f'Hello {name} ....')
    print(f"Because you from {country} Your course Price is : ${course_price-60}")
else:
    print(f'Hello {name} ....')
    print(f"Because you from {country} Your course Price is : ${course_price - 30}")