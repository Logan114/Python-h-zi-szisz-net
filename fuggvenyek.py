def elso_feladat():
    print ("Adjon meg egy számot 200 és 920 között")
    ok = False
    while ok == False:
        n = int(input("Kérem adjon meg egy számot "))
        if n < 200 or n > 920:

            if n < 200:
                print ("A szám túl alacsony! Adjon meg egy számot 200 és 920 között! ")

            if n > 920:
                print ("A szám túl magas! Adjon meg egy számot 920 alatt!")

        else:
            n = str(n)
            print(n[0])
            ok = True

def masodik_feladat(n):
    print(n//10, "Darab tizes\n", n//100, "Darab százas\n", n//1000, "Darab ezres")

def harmadik_feladat(n):
    print("Megadott számban levő számok összege\n")
    if n < 100:
        szam = str(n)
        n1:int =  int(szam[0])
        n2: int = int(szam[1])
        print (n1+n2)
    if n < 999:
        szam = str(n)
        n1:int =  int(szam[0])
        n2: int = int(szam[1])
        n3:int = int(szam[2])
        print (n1+n2+n3)
    if n < 9999:
        szam = str(n)
        n1: int = int(szam[0])
        n2: int = int(szam[1])
        n3: int = int(szam[2])
        n4: int = int (szam[3])
        print(n1 + n2 + n3 + n4)
    else:
        print("A  szám túl magas, 10000 alatti számokkal működik csak!")


def negyes_feladat(a):
    if a == 90:
        print ("Még 90% on vagyunk!")
    if a in range (2,3):
        print("Még bírjuk (60%)")
    if a in range (4,7):
        print("Progit tanulunk, töltődőnk! 70%")
    if a in range (8,9):
        print ("lassan már nem bírjuk tovább! 50%")
    if a >= 10:
        print ("Ez már tényleg túlzás")#legalább egy cigiszünetet kaphatnánk...
    if a == 0:
        print ("Már be se jövök!")

def otos_feladat(nap, ora):
    if nap == "hetfo":
        allapot = "Alszik"
    if nap == "kedd":
        if ora == "hittan":
            allapot = "Figyel"
        else:
            allapot = "Alszik"
    if nap == "szerda":
        if ora == "programozas":
            allapot = "dolgozik"
        else:
            allapot = "N/A"
    if nap == "csutortok":
        allapot = "Figyel"
    if nap == "pentek":
        allapot = "Felig van jelen"
    print ("Márti",allapot)

