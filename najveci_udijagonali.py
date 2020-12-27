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
    najmanjiudijagonali = True
    x=i
    y=j
    while x>=1 and y>=1:
      x-=1
      y-=1
      if matrica[x][y] < matrica[i][j]:
        najmanjiudijagonali = False
    x=i
    y=j
    while x>=1 and y<m-1:
      x-=1
      y+=1
      if matrica[x][y] < matrica[i][j]:
        najmanjiudijagonali = False
    x=i
    y=j
    while x<n-1 and y<m-1:
      x+=1
      y+=1
      if matrica[x][y] < matrica[i][j]:
        najmanjiudijagonali = False 
    x=i
    y=j
    while x>=1  and y<m-1:
      x-=1
      y+=1
      if matrica[x][y] < matrica[i][j]:
        najmanjiudijagonali = False  
    if najmanjiudijagonali:
      brojac+=1

    



for i in range(0,n):
  for j in range(0,m):
    print(matrica[i][j],end=' ')
  print()  

print(brojac)
  

