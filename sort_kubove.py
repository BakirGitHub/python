def cifre (n):
  lista=[]
  while(n!=0):
    cifra=n%10
    lista.append(cifra)
    n=n//10
  return lista

def zbir_kub(lista):
  zbir=0
  for i in range(len(lista)):
    zbir=zbir+(lista[i])**3
  return zbir

zbir=0
for i in range(100,1000):
  lista=cifre(i)
  zbir=zbir_kub(lista)
  if(i==zbir):
    lista.sort()
    for j in range(len(lista)):
      print(lista[j],end=" ")
    print("=", zbir)
    print()
      
    