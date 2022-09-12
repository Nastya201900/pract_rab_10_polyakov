c = 0
s1 = 0
s2 = 100
for s in open("test.txt"):
    if int(s) > 0 and int(s) % 2 == 0:
        if s1 < int(s):
            s1 = int(s)
for s in open("test.txt"):
    if int(s) > 0 and int(s) % 2 == 0:
        if s2 > int(s):
            s2 = int(s)
s3 = open("test8.txt", "w")
a = str(s1)
b = str(s2)
s3.write(a)
s3.write(" ")
s3.write(b)
print(a,b)
s3.close()