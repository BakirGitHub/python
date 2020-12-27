n = int(input("n = "))
for i in range(n):
    for j in range(n - i):
        print(" ", end = " ")
    for k in range(n):
        print("*", end = " ")
    for l in range(1):
        print(" ")
print()