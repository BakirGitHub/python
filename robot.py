import random
random.seed(42)
n=int(input())
x=0
y=0  #1 je gore, 2 je dolje, 3 je lijevo, 4 je desno
br=0

for j in range (n):
 for i in range(10):
  broj = random.randint(1, 4)
  if broj == 1:
    x = x
    y = y + 1
  elif broj == 2:
    x = x
    y = y - 1
  elif broj == 3:
    x = x - 1
    y = y
  elif broj == 4:
    x = x + 1
    y = y
  
  if x == 0 and y == 0:
    br = br + 1 
  
  if x != 0 or y != 0:
    x = 0
    y = 0
  i = i + 1 

vjerovatnoca = br / n
print("Vjerovatnoća je", vjerovatnoca)
      


    
