def meny():
    Valg = input("Her er dine valg:\nSkriv 0 for å lese en avtale fra fil\nSkriv 1 for å skrive avtalene til en fil\nSkriv 2 for å skrive en ny avtale\nSkriv 3 for å skrive ut alle avtalene\nSkriv 4 for å slette en avtale\nSkriv 5 for å redigere en avtale\nSkriv 6 for å avslutte: ")
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
        Gruppe = input("Skriv inn en gruppe av avtaler du vil redigere: ")
        liste(Gruppe, 'velg')
        valget = int(input('skriv inn indeksen'))
        print(Gruppe.get(valget))
        Gruppe.get(valget).tittel = input('skriv inn ny tittel: ')
        Gruppe.get(valget).sted = input('skriv inn nytt sted: ')
        Gruppe.get(valget).starttidspunkt = datetime.datetime(int(input("Starttidspunkt år:")), int(input("Måned:")), int(input("Dag:")), int(input("Timer:")), int(input("Minutter:")), int(input("Sekunder:")))
        Gruppe.get(valget).varighet = input('skriv inn ny varighet')
        print(Gruppe.get(valget))
    if Valg == "5":
        Gruppe = input("Skriv inn navnet av gruppen hvor du vil slette av: ")
        liste(Gruppe, 'slett')  
        valget = int(input('skriv inn indeksen'))
        Gruppe.pop(valget)
        liste(Gruppe, 'slett')
    if Valg == "6":
        print("Ha en fin dag")