n = int(input("n = "))
if (n % 2 != 0):
    print("Nije dobar unos.")
else:
    for i in range(n):
        for j in range(1):
            print(" ")
        for k in range(2 * n - i):
            print(" ", end = "")
        for l in range(i * 2 + 1):
            print("*", end = "")
    for i in range(n + 1):
        for p in range(1):
            print(" ")
        for r in range(n + i):
            print(" ", end = "")
        for s in range((2 * n + 1) - i * 2):
            print("*", end = "")
    print()