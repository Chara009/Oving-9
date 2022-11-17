import datetime

class Avtale:
    
    def __init__(self, Tittel, Sted, Starttidspunkt, Varighet):
        self.tittel = Tittel
        self.sted = Sted
        self.starttidspunkt = Starttidspunkt
        self.varighet = Varighet

    def __str__(self):
        return f"{self.tittel} \n{self.sted} \nStart dato: {self.starttidspunkt} \nVarer i {self.varighet} minutter"

    def legg_til_kategori(self, Kategori):
        self.kategori = []
        self.kategori.append(Kategori)


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




def nyttSted():
    en = input('skriv id')
    to = input('skriv navn')
    tre = input('skriv gateadresse')
    fire = input('skriv postnummer')
    fem = input('skriv poststed')
    return Sted(en, to, tre, fire, fem)

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



def lagringAvtale(avtaleListe, kategoriListe):
    file = open(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Avtaler.txt', "a")
    for avtalle in avtaleListe:
        file.write(f"{avtalle.tittel}; {avtalle.sted}; {avtalle.starttidspunkt}; {avtalle.varighet}\n")
    lagreKategori(kategoriListe)
    file.close()
    

def lesing(fil):
    gruppe = []
    i = 0
    #f = liste.readline()
    for f in fil:
        f = f.rstrip("\n")
        f = f.split(";")
        avtale = Avtale(f[0], f[1], f[2], f[3])
        gruppe.insert(len(gruppe), avtale)
        #f = liste.readline()
        i += 1
    return gruppe

#For testing av sted:
#x = Sted('5', 'navn', 'adresse', '0770', 'fem')
#,steder = [x, x, x, x, x, x]
#lagreSteder(steder, 'Steder.txt')


#liste = []
#lesing(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Steder.txt', liste)
#print(liste)


y = Kategori(1000, 'seks', 'sju')

#r = Avtale('tittel', 'etc', datetime.datetime.now(), 2)
#r.legg_til_kategori(y)
#print(r.kategori)

kategoriListe = [y, y, y, y, y]

#lesingk(r'C:\Users\Jørgen\Documents\PythonScripts\Oving9\Oving-9\Kategorier.txt', katListe)

#PrintKategori(katListe)


b = Avtale(5, 5, 5, 5)
avtaleListe = [b, b, b, b, b, b, b]
lagringAvtale(avtaleListe, kategoriListe)



'''
while i < 20:
    avtale = Avtale(i, i, i, i)
     = avtale
    i += 1
print(Gruppe)
'''