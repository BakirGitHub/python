n=int(input())
suma=0

while n>(-1):
  if (n<10):
    suma = suma + n
  else:
    suma = suma + (n//10) % 10
  n = int(input())

print(suma)