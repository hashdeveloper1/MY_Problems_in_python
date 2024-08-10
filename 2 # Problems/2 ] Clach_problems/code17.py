import sys
import math


c = input()
n = int(input())
cc = 0
for i in range(n):
    book = input()
    if book.startswith(c):
        cc += 1
print(cc)


