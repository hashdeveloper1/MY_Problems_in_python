#######################################################
#         -- Calculate Age Project version 2 --       #
#         -- BY Hashem Ahmed Mahmoud ELMahdi --       #
#######################################################
# write note like good
print('#'*40)
print(' [ You Can to Enter W or M or D ] '.center(40, '#'))
print('#'*40)
# Collect age by input
age = int(input("Enter Your Age : ").strip())
# Collect unit by input
unit = input("Enter Your Unit Age { Months , Weeks , Days }: ").strip().lower()
# =========================
# Collect Months And Days And Weeks And More As Operation Statements
month = age * 12
week = month * 4
day = week * 7
hours = day * 24
mints = hours * 60
seconds = mints * 60
# =========================
# Check Choice And Implement This Choice By Return Result
if unit == 'months' or unit == 'm':
    print("You Choose Months")
    print(f"You Lived {month:,} Months")
elif unit == 'weeks' or unit == 'w':
    print("You Choose Weeks")
    print(f"You Lived {week:,} Weeks")
elif unit == 'Days' or unit == 'd':
    print("You Choose Days")
    print(f"You Lived {day:,} Days")
else:
    print("You Lived for")
    print(f"{month} Month")
    print(f"{week:,} Week")
    print(f"{day:,} Days")
    print(f"{mints:,} Mints")
# =========================
# This Design To End Program
print('#'*40)
print(' [ End Program ] '.center(40, '#'))
print('#'*40)