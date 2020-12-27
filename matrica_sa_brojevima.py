n = int(input())

for i in range(0,n):
  print("1", end=" ")
  for j in range(1,n-i):
    print(j+1, end=" ")
  print()