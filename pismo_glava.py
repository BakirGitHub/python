import random

n = eval(input())
if n < 0 or n > 1:
  print("pogresan unos")
else:
  x = random.randrange(0,2)
  if x==0:
    print("pismo je! ")
  else:
    print("glava je!")