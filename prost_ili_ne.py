#ispitati da li je broj prost

n = int(input("unesi broj: "))
b = 0 

for i in range (1, n+1):
  if (n % i == 0):
    b+=1
if (b==2):
  print("prost je")
else:
  print("nije prost")
