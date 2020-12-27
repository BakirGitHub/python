import random
random.seed(42)

zbirKoraka=0
for i in range(0,10000):
  brojacBacanja=0
  brojacSestica=0
  
  while True:
    a = random.randint(1 , 6)
    b = random.randint (1 , 6)

    zbir = a+b
    brojacBacanja+=1

    if (zbir > 6):
      brojacSestica+=1
    else:
      brojacSestica==0
    if brojacSestica==3:
      zbirKoraka+=brojacBacanja
      print("trebalo nam je: ", brojacBacanja)
      break
print(zbirKoraka/10000)

