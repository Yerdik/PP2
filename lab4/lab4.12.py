import math

num_sides = 4
length = 25

area = (num_sides * length ** 2) / (4 * math.tan(math.pi / num_sides))

print("Input number of sides:", num_sides)
print("Input the length of a side:", length)
print("The area of the polygon is:", round(area, 2))