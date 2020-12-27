from math import sqrt

xA = int(input("unesi koordinatu x prvog kruga: "))
yA = int(input("unesi koordinatu y prvog kruga: "))

xB = int(input("unesi koordinatu x drugog kruga: "))
yB = int(input("unesi koordinatu y drugog kruga: "))

r1 = float(input("unesi poluprecnik prvog kruga: "))
r2 = r1/2 

if r1+r2>sqrt((xA-xB)**2 + (yA - yB)**2):
  print("sijeku se")
else:
  print("ne sijeku se")
