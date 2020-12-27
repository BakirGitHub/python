#ispisati sve proste brojeve do tog broja
n = int(input("unesi broj: "))

for i in range (1, n+1):
  b=0
  for k in range(1,i+1):
    if (i%k==0):
      b+=1
  
  if (b==2):
    print(i)
