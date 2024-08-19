# -------------------------------------------- string method
# ord()
# len()
# str()
# int()
# st1.count('o')
# s.split('-')
# s.center(5, '@')
# s.rsplit(',', 2)
# s.swapcase()
# s.startswith('i')
# s.endswith('+')
# s.endswith('++')
# --------------------------------------------

# --------------------------------------------
# -- count method --

st1 = ".....o......o......ooo.....oo....o"

print(st1.count('o')*8)
print(st1.count('o', 0,41))

# ---------------------------------------------
# -- split method --
# -----------------
s = "I Love Python And C++"
print(s.split())
# -----------------
s = "I-Love-Python-And-C++"
print(s.split('-'))
# -----------------
s = "I-Love-Python-And-C++"
print(s.split('-', 1))
# ------------------
s = "I,Love,Python,And,C++"
print(s.split(','))
c = 0
for i in s.split(','):
    c += 1
    print(f"Colum {c}: {i}")
# ------------------
s = "I,Love,Python,And,C++"
print(s.rsplit(',', 2))
# -------[ End ]--------
# ---------------------------------------------
# -- center method --
# -----------------
s = "Hashem"
print(s.center(len(s)+4))  # length string
# -----------------
s = "Hashem"
print(s.center(len(s)+6, '*')) # length string and fillchar '@' one char only
# -------[ End ]--------
# ---------------------------------------------
# -- count method --
# -----------------
s = "I Love Python And C++"
print(s.count('n'))  # search on any char or any string
# -----------------
s = "I Love Python And C++"
print(s.count('n', 0, 15))  # search on any char or any string and take start index and end index
# -------[ End ]--------
# ---------------------------------------------
# --  swapcase method --
# -----------------
s = "Hashem"
print(s.swapcase())
print((s.swapcase()).swapcase())  # convert any char capitalize to small and reversing
# -------[ End ]--------
# ---------------------------------------------
# --  starttwith method --
# ---------------------
s = "I Love Python And C++"
print(s.startswith('i'))
print(s.startswith('I L'))
# ---------------------
s = "I Love Python And C++"
print(s.startswith('P', 7, 10))
print(s.startswith('I L',0, 3))
# -------[ End ]--------
# ---------------------------------------------
# --  Endtwith method --
# ---------------------
s = "I Love Python And C++"
print(s.endswith('+'))
print(s.endswith('++'))
# ---------------------
s = "I Love Python And C++"
print(s.endswith('++', 0, len(s)))
print(s.endswith('I L',0, 3))
# -------[ End ]--------
# ---------------------------------------------
