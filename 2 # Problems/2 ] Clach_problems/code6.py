import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input().split()
s = ''
for i in message:
    if len(i) % 2 == 0:
        s += i[int(len(i) / 2)-1]
    else:
        s += i[int(len(i)/2)]
print(s)