
class Sted:
    def __init__(self, id, navn, gateadresse = 'none', postnummer = 'none', poststed = 'none'):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
    
    def __str__(self):
        return f'{self.id}, {self.navn}'

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

def lesing(fil, list):
    lesingFil = open(fil, "r")
    for f in lesingFil:
        f = f.rstrip("\n")
        f = f.split(";")
        sted = Sted(f[0], f[1], f[2], f[3], f[4])
        list.insert(len(list), sted)
    lesingFil.close()


x = Sted('5', 'navn', 'adresse', '0770', 'fem')
steder = [x, x, x, x, x, x]
lagreSteder(steder, 'Steder.txt')

#liste = []
#lesing('Steder.txt', liste)
#print(liste)



