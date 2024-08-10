import sys
import math

n = int(input())

for i in range(n):
    print(' '.join((i+1) * '*'))
for i in range(n-1, 0, -1):
    print(' '.join(i * '*'))

