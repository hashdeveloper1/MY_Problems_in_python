n = int(input())
for i in range(n):
    s = input()
    if s.find('010') > -1 or s.find('101') > -1:
        print("Good")
    else:
        print("Bad")

