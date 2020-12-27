n = int(input("unesi cetverocifren broj"))

if (n<1000 and n>10000):
  print("unesi cetverocifren broj: ")

a = (n//10)//100 
b = ((n//10)//10)%10
c = (n//10)%10
d = (n%10)

if (a<b and b<c and c<d):
  print("u neopadajucem su nizu")
else:
  print("u nekom su drugom obliku ali nisu u neopadajucem")



