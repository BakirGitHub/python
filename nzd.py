n = int(input("unesi broj: "))
m = int(input("unesi broj: "))

if (n<m):
  najmanji=n
else:
  namanji=m

for i in range (1, namanji+1):
  if (n%i==0 and m%i==0):
    nzd = i

print ("nzd od brojeva m i n je: ",nzd)

