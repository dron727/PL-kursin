import math

x = (16.55 * 10 ** (-3))
y = (-2.75)
z = (0.15)

s1 = math.sqrt(10*((x**(1/3)+x**(y+2))))

s2 = (math.asin(z) ** 2) - (abs(x-y))

s = s1 * s2

print(s)