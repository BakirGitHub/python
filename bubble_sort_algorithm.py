x = int(input("unesite petocifren : "))

lista=[]
if (x<10000 and x>100000):
  print("unesite petocifren broj!!!")
else:
  while(x!=0):
    cifra = x%10
    lista.append(cifra)
    x = x//10
for i in range(len(lista)):
  for j in range(len(lista)):
    if(lista[i]<lista[j]):
      c=lista[i]
      lista[i]=lista[j]
      lista[j]=c
print(lista)
