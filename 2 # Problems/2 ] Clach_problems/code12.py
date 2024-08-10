import sys
import math


statements = input().split()
print(statements)
c =0
for i in statements:
   if i == 'inc':
      c +=1
   elif i == 'dec':
      c -= 1
   elif i == 'double':
       c += c
   elif i == 'half':
       c += c//2
   elif i == 'print':
       break
   elif i == 'exit':
       break
print(c)
# dec dec double doubleprint(c) double double double double double inc inc inc inc dec inc half print exit
