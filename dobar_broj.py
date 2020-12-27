x = int(input("unesite trocifren broj: "))
if (x<100 and x>1000):
  print("unesi trocifren broj")

a = (x // 100)
b = (x//10)%10
c = (x%10)%10

if ( c-1==a or a-1==c or a-1==b or b-1==a or c-1==b or b-1==c):
  print("broj je dobar") 
else:
  print("broj nije dobar")