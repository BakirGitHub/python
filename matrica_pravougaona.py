n = int(input())

for i in range(0,n):
  for j in range(0,n*2):
    if (i==0 or i==n-1  or j==0 or j==n):
      print("x", end=" ")
  print()