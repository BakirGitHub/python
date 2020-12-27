from math import radians

a = int(input("unesi ugao alfa: "))
b = int(input("unesi ugao beta: "))
c = int(input("unesi duzinu stranice trogula: "))

g = 180 - (a + b)
k = radians(g)

l = radians(a)
t = radians(b)

r = c*((sin(l)/2)*(sin(t)/2))/(cos(k)/2)

print(r)
