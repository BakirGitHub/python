def fibonacci(n, c):
    a=1
    b=0
    c=open("m.txt", 'a')
    lista=[]
    
    for i in range(0,n):
       b=b+a
       a=b-a
       lista.append(b)
    for i in range(0, len(lista)):
      if i==(len(lista)-1):
        c.write(str(lista[len(lista)-1]))
      else:
        c.write(str(lista[i]))
        c.write(" , ")
       
n=int(input("unesite broj"))
c=input("unesite naziv fajla:")
fibonacci(n,c)


