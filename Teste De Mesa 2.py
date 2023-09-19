a = [4,5,6]
b = a * 2
c = a[:]
d = a
a[0] = 'a'
b[0] = 'b'
c[0] = 'c'
d[0] = 'd'
print(a)
print(b)
print(c)
print(d)