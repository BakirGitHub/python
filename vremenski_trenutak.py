print("unesi prvi vremenski momenat: ")
x = int(input("unesi sate za prvi vremenski momenat: "))
y = int(input("unesi minute za prvi vremenski momenat: "))
z = int(input("unesi sekunde za prvi vremenski momenat: "))

print("unesi drugi vremenski momenat")
a = int(input("unesi sate za drugi vremenski momenat: "))
b = int(input("unesi minute za drugi vremenski momenat: "))
c = int(input("unesi sekunde za drugi vremenski momenat: "))

prvi = (x*3600 + y*60 + z)
drugi = (a*3600 + b*60 + c)

if (prvi<drugi):
  print("prvi vremenski momenat je prije drugog")
elif (prvi>drugi):
  print("prvi vremenski momenat je poslije drugog")
else: 
  print("jednaki su")