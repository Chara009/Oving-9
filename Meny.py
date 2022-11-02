def meny():
    Valg = input("Her er dine valg:\nSkriv 0 for å lese en avtale fra fil\nSkriv 1 for å skrive avtalene til en fil\nSkriv 2 for å skrive en ny avtale\nSkriv 3 for å skrive ut alle avtalene\nSkriv 4 for å avslutte: ")
    if Valg == "0":
        doc = input("Skriv inn navnet av dokumentet: ")
        Fil = open(doc, "r")
        Gruppe = lesing(Fil)
    if Valg == "1":
        Gruppe = input("Skriv inn navnet av gruppen med avtaler: ")
        lagring(Gruppe)
    if Valg == "2":
        Avtale = Inp()
    if Valg == "3":
        Gruppe = input("Skriv inn navnet av gruppen med avtaler til å lese: ")
        Overskrift = input("Skriv inn overskrift: ")
        liste(Gruppe, Overskrift)
    if Valg == "4":
        print("Ha en fin dag")