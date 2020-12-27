def suma(n):
  suma=0
  if n>0:
    while n!=0:
      cifra=n&10
      suma+=cifra
      n=n//10
  elif n<0:
    n=n*(-1)
    while n!=0:
      cifra=n&10
      suma+=cifra
      n=n//10
  elif n==0:
    suma=0
  return suma

def najveci(lista):
  najveci=0
  pozicija=0
  for i in range(len(lista)):
    if (suma(lista[i]))>najveci:
      najveci=suma(lista[i])
      pozicija=i
  return lista[pozicija]

lista=[1,2,-3,-66]
print(najveci(lista))


