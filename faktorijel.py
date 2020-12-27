def sumacifara(n):
  f=1
  for i in range(0,n):
    f=f*(i+1)
    brojac=0
  while f>0:
    a = f%10
    f=f//10
    brojac=brojac + a
  return(brojac)

print(sumacifara(5))