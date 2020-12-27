n=int(input("unesi neparan broj:"))
lista=[]
for i in range(n):
    a=int(input("unesi brojeve:"))
    lista.append(a)
lista2=[]
for i in range(0,n):
    lista2.append(lista[i])
lista2.sort()
c=lista2[int(len(lista2)/2)]
for i in range(0,len(lista)):
    if lista[i]==c:
        lista2.remove(c)
        break
for i in range(len(lista2)):
    print(lista2[i],(" "), end="")