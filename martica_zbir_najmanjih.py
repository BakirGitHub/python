n=int(input())
m=int(input())

matrica=[]

for i in range(0,n):
  matrica.append([0]*m)


for i in range(0,n):
  for j in range(0,m):
    matrica[i][j]= int(input())
    
zbir_najmanjih=0

for i in range(0,n):
  najmanji= matrica[i][0]
  for j in range(1,m):
    if najmanji > matrica[i][j]:
      najmanji = matrica[i][j]
  zbir_najmanjih+=najmanji
    



for i in range(0,n):
  for j in range(0,m):
    print(matrica[i][j],end=' ')
  print()  

print(zbir_najmanjih)
  
