file = """,,,
Hashem,20000,24,Male
Ali,30000,,Male
Abdo,20000,20,Male
"""

lines, l = file.splitlines(), []
c = 0

for i in lines:
    line = i.split(',')
    c += 1
    print("----------------------------------------")
    print(f"Employee {c}")
    print(f"Name : {line[0]}")
    print(f"Salary : {line[1]}")
    print(f"Age : {line[2]}")
    print(f"Gender : {line[3]}")
    print("----------------------------------------")
    print(",".join(line))
