n=int(input())
m=int(input())

matrica=[]

for i in range(0,n):
  matrica.append([0]*m)


for i in range(0,n):
  for j in range(0,m):
    matrica[i][j]= int(input())
    
brojac=0

for i in range(0,n):
  for j in range(0,m):
    najmanjiukoloni = True
    for k in range(0,n):
      if matrica[k][j] < matrica[i][j]:
        najmanjiukoloni=False
  
  najveciUredu=True
  for k in range(0,m):
    if matrica[i][k] > matrica[i][j]:
      najveciUredu=False


  if najmanjiukoloni and najveciUredu:
    brojac+=1

    



for i in range(0,n):
  for j in range(0,m):
    print(matrica[i][j],end=' ')
  print()  

print(brojac)
  

