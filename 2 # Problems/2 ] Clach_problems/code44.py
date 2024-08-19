#  -- Hash Clash --
# s = ' '.join(c for c in s.lower() if c.isalpha())
# if s[::-1]==s:print("");exit()
# from itertools import cycle
# C = cycle([10,6,0,10,6,24])
# while 1: print(next(C))
# print(chr(48))  # convert from Asscicode into char
# from collections import defaultdict
# # Create a defaultdict with a default value of 0
# dic = defaultdict(int)
# import sys
# import math
#
# floor = int(input())
# print("#  #")
# for i in range(floor):
#     print("####\n#  #")

# int f;
# cin >> f;
# cout<<"#  #";
# for(int i ;i<f;i++){
#     cout<<"####\n#  #";
# }
import sys
import math
p = int(input())
h = int(input())
r = int(input())
if p * h >= r:
    print("Yes")