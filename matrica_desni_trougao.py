n = int(input())

for i in range(0,n):
  for j in range(0,n):
    if (i+j==n-1 or j==n-1 or i==n-1 or j+i==n or j-2+i==n or i+j==n+1 or i+j==n+2 or i+j==n+3):
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()