n=int(input("unesi broj n:"))
lista=[]
for i in range(n):
    a=int(input("unesi brojeve liste:"))
    lista.append(a)
m=int(input("unesite broj m:"))
lista.sort()
lista2=lista[m:(len(lista)-m)]
for i in range(len(lista2)):
    print(lista2[i],(" "), end="")