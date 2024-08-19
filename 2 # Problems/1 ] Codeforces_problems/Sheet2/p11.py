n = input()
s = list(input())

def insertion_sort(s):
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key
    return s

s = insertion_sort(s)
print(''.join(s))