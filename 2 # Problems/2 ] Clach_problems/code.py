import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
l = []
c = 0
for i in line:
    if i != ' ':
        l.append(c)
        c = 0
    c += ord(i)
l.append(c)

for i in l:
    print(i)
