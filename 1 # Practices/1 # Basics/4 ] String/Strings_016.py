########################################################################################################################
########################################################################################################################
# ------ string method ------
# ord()
# len()
# str()
# int()
# (s.zfill(5)
# str1.strip()
# str1.rstrip()
# str1.lstrip()
# str1.title()
# str1.capitalize()
# str1.upper()
# str1.lower()
# st1.count('o')
# s.split('-')
# s.center(5, '@')
# s.rsplit(',', 2)
# s.swapcase()
# s.startswith('i')
# s.endswith('+')
# s.endswith('++')
# s.index('chORstr',S,E) return index or error
# s.find('chORstr',S,E) return index or -1
# s.rjust(20, '+') length and fill right by ch '+'
# s.ljust(20, '+') length and fill left by ch '+'
# s.splitlines() ['Line 1', 'Line 2', 'Line 3']
# s.expandtabs(10) # number tabs  = 'Hello\tPython\tC++\tJS\tHTML'
# s.istitle()  # return true or flase
# s.ispace()  # return true or flase s = " " true
# s.isupper() return true or flase
# s.islower() return true or flase
# s1.isidentifier()
# s.isalpha() only alpha
# s.isalnum()  only alpha or numbers or mix
# s.isnumeric() only numbers
# left_padding = ('{:+>5}'.format(str1))
# print(str2[0:1])
# print(str2[::1])   # print by step 1
# print(str2[0::2])  # print by step 2
# print(str2[0::3])
# s.replace('World','Python')  # s = "Hello World Hello"
########################################################################################################################
########################################################################################################################
s = "Hello World Hello World"
print(s.replace('World', 'Python'))
print(s.replace('world', 'Python'))
print(s.replace('World', 'Python', 1))
print(s.replace('World', 'Python', 2))
# --------------------------------------------------------------
s = ['Hello', 'World', 'Hello', 'World']
print(",".join(s))


########################################################################################################################
