import random

def generisiOdgovor(t):
    return t + random.randint(-(t/2)//1, (t/2)//1)

def generisiBroj():
    rezultat = 10
    return rezultat

def generisiOperaciju():
    return random.randint(0, 3)

def cijeloPitanje():
    # Generisemo a
    a = generisiBroj()
    # Generisemo b
    b = generisiBroj()

    # Generisemo operaciju
    o = generisiOperaciju()

    # Spasimo negdje tacan rezultat
    if (o == 0):
        rezultat = a + b
        operacija_znak = '+'
    elif (o == 1):
        rezultat = a - b
        operacija_znak = '-'
    elif (o == 2):
        rezultat = a * b
        operacija_znak = '*'
    else:
        rezultat = a / b
        operacija_znak = '/'

    # Generisemo tri slucajna rezultata (po mogucnosti logicna)
    odgovor_a = generisiOdgovor(rezultat)
    odgovor_b = generisiOdgovor(rezultat)
    odgovor_c = generisiOdgovor(rezultat)

    # ispisemo pitanje
    print("Izracunajte", a, operacija_znak, b, "=")

    pozicija_rezultata = random.randint(1, 4)

    if pozicija_rezultata == 1:
        print("1)", rezultat)
        print("2)", odgovor_a)
        print("3)", odgovor_b)
        print("4)", odgovor_c)

    if pozicija_rezultata == 2:
        print("1)", odgovor_a)
        print("2)", rezultat)
        print("3)", odgovor_b)
        print("4)", odgovor_c)

    if pozicija_rezultata == 3:
        print("1)", odgovor_a)
        print("2)", odgovor_b)
        print("3)", rezultat)
        print("4)", odgovor_c)

    if pozicija_rezultata == 4:
        print("1)", odgovor_a)
        print("2)", odgovor_b)
        print("3)", odgovor_c)
        print("4)", rezultat)

    odgovor = int(input("Unesite svoj odgovor: "))

    while odgovor < 1 or odgovor > 4:
        odgovor = int(input("Unesite svoj odgovor: "))

    if (odgovor == pozicija_rezultata):
        print("Odgovor je tacan!")
        return True

    print("Odgovor je netacan!")
    return False
    # korisnik bira odgovor

    # provjerimo je li tacan odgovor


while(cijeloPitanje()):
    print("Evo ti novo pitanje!")