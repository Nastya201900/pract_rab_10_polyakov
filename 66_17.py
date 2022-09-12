s = [input() for i in range(5)]
def qq(s):
    if len(s) == 1 or len(s) == 0:
        return s
    h = s[0]
    less = [i for i in s[1:] if i <= h]
    greater = [i for i in s[1:] if i > h]
    return qq(less) + [h] + qq(greater)
newlist = qq(s)
s = [el[3:] for el in s]
print(*s, sep=', ')