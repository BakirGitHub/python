def stepen(a,b):
  f=0
  for i in range(1,10000):
    if (a==b**i):
      f=1
      print("stepen je")
      break
  if (f!=1):
    print("nije stepen")
a=int(input())
b=int(input())
stepen(a,b)