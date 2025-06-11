def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = 2
b = 6
for val in squares(a, b):
    print(val)