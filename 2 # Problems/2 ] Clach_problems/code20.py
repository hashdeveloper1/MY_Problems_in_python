# # -- Hash Clash --
def revers_str(s): return s[::-1]

n = int(input())
s = ''
for i in range(1,n+1): s += str(i)
print(s*n)