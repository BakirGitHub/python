n=int(input())
m=int(input())

matrica=[]

for i in range(0,n):
  matrica.append([0]*m)


for i in range(0,n):
  for j in range(0,m):
    matrica[i][j]= int(input())
    
for i in range(0,n):
  for j in range(0,m//2):
    x=matrica[i][j]
    matrica[i][j]=matrica[i][m-1-j]
    matrica[i][m-1-j]=x

for i in range(0,n):
  for j in range(0,m):
    print(matrica[i][j],end=' ')
  print()
