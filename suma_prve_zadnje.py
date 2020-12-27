n = int(input())

lista=[]
while n>0:
    cifra=n%10
    n=n//10
    lista.append(cifra)

suma=(lista[0]+lista[-1])
print(suma)
