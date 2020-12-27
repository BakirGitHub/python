n=int(input())
m=int(input())

matrica=[]

for i in range(0,n):
  matrica.append([0]*m)


for i in range(0,n):
  for j in range(0,m):
    matrica[i][j]= int(input())
    
'''zbir_najmanjih=0

for i in range(0,n):
  najmanji= matrica[i][0]
  for j in range(1,m):
    najmanji=matrica[0][j]
    if najmanji > matrica[i][j]:
      najmanji = matrica[i][j]
  zbir_najmanjih+=najmanji
    



for i in range(0,n):
  for j in range(0,m):
    print(matrica[i][j],end=' ')
  print()  

print(zbir_najmanjih)'''
  
def najmanjiuredu(matrica):
  suma=0
  for i in range(0,n):
    najmanji= matrica[i][0]
    for j in range(1,m):
      if najmanji > matrica[i][j]:
        najmanji = matrica[i][j]
    suma+=najmanji
  return suma

def najmanjikolona(najmanji=matrica[0][j]matrica):
  suma=0
  for j in range(0,m):
    najmanji=matrica[0][j]
    for i in range(1,n):
      if najmanji > matrica[i][j]:
        najmanji = matrica[i][j]
    suma+=najmanji
  return suma

print(najmanjiuredu(matrica))
print(najmanjikolona(matrica))
