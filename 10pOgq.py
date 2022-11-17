import datetime

class Avtale:
    
    def __init__(self, Tittel, Sted, Starttidspunkt, Varighet):
        self.tittel = Tittel
        self.sted = Sted
        self.starttidspunkt = Starttidspunkt
        self.varighet = Varighet
        self.kategori = []

    def legg_til_kategori(self, Kategori):
        self.kategori.append(Kategori)
        ferdig = ''
        for k in self.kategori:
            ferdig = ferdig + f'{k.navn}, '
        self.kategoriStreng = ferdig

    def __str__(self):
        return f"{self.tittel} \n{self.sted} \nStart dato: {self.starttidspunkt} \nVarer i {self.varighet} minutter\nKategorier: {self.kategoriStreng}"


class Sted:
    def __init__(self, id, navn, gateadresse = 'none', postnummer = 'none', poststed = 'none'):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
    
    def __str__(self):
        return f'{self.id}, {self.navn}'

class Kategori:
    
    def __init__(self, Id, Navn, Prioritet):
        self.id = Id
        self.navn = Navn
        self.prioritet = Prioritet
        
    def __str__(self):
        return f"{self.id} \n{self.navn} \nPrioritet: {self.prioritet}"

def nyKategori():
    Id = input("Skriv ID: ")
    Navn = input("Skriv navn: ")
    Prioritet = input("Skriv prioritet: ")
    kategori = Kategori(Id, Navn, Prioritet)
    return kategori

def lagreKategori(list):
    kategoriFil = open(r"C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Kategorier.txt", "a")
    for u in range(len(list)):
        kategoriFil.write(f"{list[u].id}; {list[u].navn}; {list[u].prioritet}\n")
    kategoriFil.close()

def lesingk(fil, liste):
    kategoriFil = open(fil, "r")
    for c in kategoriFil:
        print(c)
        c = c.rstrip("\n")
        print(c)
        c = c.split("; ")
        print(c)
        
        kategori = Kategori(c[0], c[1], c[2])
        liste.insert(len(liste), kategori)
    kategoriFil.close()

def PrintKategori(liste):
    for n in range(len(liste)):
        print(liste[n].id, "\n", liste[n], "\n")

def visOgVelgKategori(liste):
    for l in liste:
        print(l)
    valg = int(input("velg indeks for kategori"))
    return liste[valg]

def visOgVelgAvtale(liste):
    for l in range(len(liste)):
        print(l)
        print(liste[l])
    valg = int(input("velg indeks for avtale"))
    return liste[valg]
    




def nyttSted():
    en = input('skriv id')
    to = input('skriv navn')
    tre = input('skriv gateadresse')
    fire = input('skriv postnummer')
    fem = input('skriv poststed')
    return Sted(en, to, tre, fire, fem)

def visOgVelgSted(liste):
    for l in liste:
        print(l)
    valg = int(input("velg indeks for sted"))
    return liste[valg]
    

def lagreSteder(list):
    #Linja under funker ikke på min (jørgens) maskin, det funker kanskje i spyder for dere. (vs code greie)
    stedFil = open('Steder.txt', "a")
    listeLengde = len(list)
    for i in range(listeLengde):
        stedFil.write(f'{list[i].id}; {list[i].navn}; {list[i].gateadresse}; {list[i].postnummer}; {list[i].poststed}\n')
    stedFil.close()

def lesingSted(file, liste):
    lesingFil = open(file, "r")
    for f in lesingFil:
        
        f = f.rstrip("\n")
        f = f.split("; ")
        
        sted = Sted(f[0], f[1], f[2], f[3], f[4])
        liste.insert(len(liste), sted)
    lesingFil.close()


def lagringAvtale(liste):
    file = open(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Avtaler.txt', "w")
    for avtalle in liste:
        file.write(f"{avtalle.tittel}; {avtalle.sted}; {avtalle.starttidspunkt}; {avtalle.varighet}; {avtalle.kategori}\n")
    file.close()





def Inp(liste):
    try:
        Tittel = input("Tittel av avtalen:")
        if not Tittel.isalpha():
            print("Prøv på nytt")
            Inp()
        Sted = visOgVelgSted(steder)
    
        Tid = datetime.datetime(int(input("Starttidspunkt år:")), int(input("Måned:")), int(input("Dag:")), int(input("Timer:")), int(input("Minutter:")), int(input("Sekunder:")))
        Varighet = int(input("Varighet av avtalen:"))
        avtale = Avtale(Tittel, Sted, Tid, Varighet)
        liste.append(avtale)
    except ValueError:
        print("Prøv på nytt")
        Inp()
        
        
def liste(gruppe, overskrift):
    print(overskrift, "\n")
    for key in gruppe:
        print(key, "\n", gruppe[key], "\n")



def lagring(gruppe):
    file = open(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Avtaler.txt', "w")
    for key in gruppe:
        avtalle = gruppe.get(key)
        file.write(f"{avtalle.tittel}; {avtalle.sted}; {avtalle.starttidspunkt}; {avtalle.varighet}\n")
    file.close()

def lesing(liste):
    gruppe = []
    i = 0
    #f = liste.readline()
    for f in liste:
        f = f.rstrip("\n")
        f = f.split(";")
        avtale = Avtale(f[0], f[1], f[2], f[3])
        gruppe.insert(len(gruppe), avtale)
        #f = liste.readline()
        i += 1
    return gruppe

def datocheck(liste, dato):
        for u in liste:
            u = u.rstrip("\n")
            u = u.split(";")
            print(u)
            if u[3] == dato:
                print('hhhh')
                avtallle = Avtale(u[0], u[1], u[2], u[3])
                gruppe.update(u[1], avtallle)
        liste.close()   

def menyvalgRediger():
    liste(Gruppe, 'velg')
    valget = int(input('skriv inn indeksen'))
    print(Gruppe.get(valget))
    Gruppe.get(valget).tittel = input('skriv inn ny tittel: ')
    Gruppe.get(valget).sted = input('skriv inn nytt sted: ')
    Gruppe.get(valget).starttidspunkt = datetime.datetime(int(input("Starttidspunkt år:")), int(input("Måned:")), int(input("Dag:")), int(input("Timer:")), int(input("Minutter:")), int(input("Sekunder:")))
    Gruppe.get(valget).varighet = input('skriv inn ny varighet')
    print(Gruppe.get(valget))

def sjekkSted(stedListe, avtaleListe):
    for l in stedListe:
        print(l)
    valg = int(input("velg indeks for stedet du vil sjekke"))
    for d in avtaleListe:
        if d.sted.navn == stedListe[valg].navn:
            print(d)
    




def meny():
    while True:
        Valg = input("Her er dine valg:\nSkriv 0 for å lese en avtale fra fil\nSkriv 1 for å skrive avtalene til en fil\nSkriv 2 for å skrive en ny avtale\nSkriv 3 for å skrive ut alle avtalene\nSkriv 4 for å slette en avtale\nSkriv 5 for å redigere en avtale\nSkriv 6 for å legge til sted\nSkriv 7 for å legge til ny kategori\nSkriv 8 for å legge kategori til en avtale\nSkriv 9 for å sjekke hvilke avtaler er satt på et sted\nSkriv 10 for å avslutte: ")
        if Valg == "0":
            doc = str(input("Skriv inn navnet av dokumentet: "))
            Fil = open(doc, "r")
            Gruppe = lesing(Fil)
            print(Gruppe)
        if Valg == "1":
            Gruppe = input("Skriv inn navnet av gruppen med avtaler: ")
            lagring(Gruppe)
        if Valg == "2":
            Inp(avtaleListe)
        if Valg == "3":
            Overskrift = (input("Skriv inn overskrift: "))
            liste(Gruppe, Overskrift)
        if Valg == "4":
            menyvalgRediger()
        if Valg == "5":
            liste(Gruppe, 'slett')  
            valget = int(input('skriv inn indeksen'))
            a = Gruppe.pop(valget)
            print(f"Ble slettet: {a}")
            liste(Gruppe, 'slett')
        
        if Valg == "6":
            steder.append(nyttSted())
        if Valg == "7":
            kategoriListe.append(nyKategori())
        if Valg == "8":
            visOgVelgAvtale(avtaleListe).legg_til_kategori(visOgVelgKategori(kategoriListe))
        if Valg == "9":
            sjekkSted(steder, avtaleListe)
        if Valg == "10":
            print("Ha en fin dag")
            break



#r = Avtale('tittel', 'etc', datetime.datetime.now(), 2)


Fil = open("Avtaler.txt", "r")
kategoriListe = []
for o in range(10):
    y = Kategori(o, o, o)
    kategoriListe.append(y)



steder = []
for i in range(10):
    x = Sted(i, i, i, i, i)
    steder.append(x)
r = Avtale('tittel', steder[0], datetime.datetime.now(), 2)
r.legg_til_kategori(kategoriListe[1])
r.legg_til_kategori(kategoriListe[2])
r.legg_til_kategori(kategoriListe[3])
g = Avtale('tittel', steder[5], datetime.datetime.now(), 2)
g.legg_til_kategori(kategoriListe[1])
avtaleListe = [r, r, r, r, g]


#lagreSteder(steder, 'Steder.txt')


#liste = []
#lesing(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Steder.txt', liste)
#print(liste)



meny()



