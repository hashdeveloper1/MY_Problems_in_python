import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_1 = input()
n_2 = input()
s = ''
for i in range(len(n_1)):
    if n_2[i] == '1' and n_1[i] == '1':
        s += '1'
    else:
        s += '0'
print(s)

