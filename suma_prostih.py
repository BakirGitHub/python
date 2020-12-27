n = int(input("unesi n:"))
m = int(input("unesi m:"))
suma=0

for i in range(n+1,m):
  prost = True
  if (i%2==0):
    prost = False
  for j in range (3,i):
    if (i%j==0):
      prost=False
  if (prost==True):
    suma+=i

print(suma) 









