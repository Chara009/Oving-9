class Kategori:
    
    def __init__(self, Id, Navn, Prioritet):
        self.id = Id
        self.navn = Navn
        self.prioritet = Prioritet
        
    def __str__(self):
        return f"{self.id} \n{self.navn} \nPrioritet: {self.prioritet}"

def inp():
    Id = input("Skriv ID: ")
    Navn = input("Skriv navn: ")
    Prioritet = input("Skriv prioritet: ")
    kategori = Kategori(Id, Navn, Prioritet)
    return kategori

def lagringk(gruppe):
    file = open("Kategorier.txt", "w")
    for key in gruppe:
        kategori = gruppe.get(key)
        file.write(f"{kategori.id}; {kategori.navn}; {kategori.prioritet}")
    file.close()

def lesingk(liste):
    gruppeK = {}
    i = 0
    f = liste.readline()
    while f != "":
        f = f.rstrip("\n")
        f = f.split(";")
        kategori = Kategori(f[0], f[1], f[2])
        gruppeK[i] = kategori
        f = liste.readline()
        i += 1
    return gruppeK

def PrintK(gruppe):
    for key in gruppe:
        print(key, "\n", gruppe[key], "\n")