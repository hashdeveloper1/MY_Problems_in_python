import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
r = ''
for i in s:
    if i.isalnum():
        r += '1'
    else:
        r += '0'
print(r)