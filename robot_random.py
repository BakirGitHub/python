import random
random.seed(42)

def random_hod(n):  
  x=0
  y=0

  for i in range(n):
    korak = random.choice(['1', '2', '3', '4'])
    if korak=='1':
      y= y+1
    elif korak == '2':
      y= y-1
    elif korak == '3':
      x= x-1
    else:
      x= x+1
  return (x,y)

for i in range(0,100000):
  hod = random_hod(10)
  
  

    