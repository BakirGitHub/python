a = int(input("unesi broj: "))
b = int(input("unesi broj: "))
c = int(input("unesi broj: "))

suma = 0

if (a==b or b==c or c==a):
  suma+=1
if suma==1:
  print("postoje dva jednaka broja")
else:
  print("svi brojevi su razlicit")
