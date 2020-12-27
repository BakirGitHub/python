from math import abs
n = int(input())

m = n
brojNaopako = 0
while m>0:
    cifra=m%10
    m = m//10
    brojNaopako = 10 * brojNaopako + cifra
    razlika = abs(n-brojNaopako)
print(razlika)


  