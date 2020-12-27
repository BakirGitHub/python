import random 
sumaTrouglova=0
brojSimulacija=10000

a=random.randint(1,1000)  
b=random.randint(1,1000)
c=random.randint()

if (a+b<c or b+a<c or c+a<b):
  trougao=0
if trougao==1:
  sumaTrouglova+=1

print(sumaTrouglova/brojSimulacija)