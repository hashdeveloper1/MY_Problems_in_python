age = int(input("Enter Your Age : ").strip())
# =========================
month = age * 12
week = month * 4
day = week * 7
hours = day * 24
mints = hours * 60
seconds = mints * 60
# =========================
print("You Lived for")
print(f"{month} Month")
print(f"{week:,} Week")
print(f"{day:,} Days")
print(f"{mints:,} Mints")
# =========================
