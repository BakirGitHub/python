n=int(input())
m=int(input())

brojac = 0
lista=[]
for i in range(n,m+1):
  x=i
  suma=0
  while (x > 0):
    suma +=(x%10)
    x = x//10
  if i % suma ==0:
    brojac=brojac+1
    lista.append(i)
print("brojevi koji ispunjavaju uslov: ",lista)
print("broj brojeva: ",brojac)