# If both a
#  and b
#  are divisible by k
# , both of them win and you should print "Both".
# If a
#  is divisible by k
#  but b
#  isn't, Memo wins and you should print "Memo".
# If b
#  is divisible by k
#  but a
#  isn't, Momo wins and you should print "Momo".
# If both a
#  and b
#  are not divisible by k
# , no one wins and you should print "No One".
c = input()
if c == 'z':
    print('a')
else:
    print(chr(ord(c)+1))
