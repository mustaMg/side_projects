a = 0
b = 1
c = 2
d = a + b + c
while a + b + c <= 1000:

    a += 1
    b += 1
    c += 1
    if a ** 2 + b ** 2 == c ** 2:
        print(a, b, c)
        print(a * b * c)
