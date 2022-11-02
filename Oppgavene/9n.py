import datetime

class Avtale:
    
    def __init__(self, Tittel, Sted, Starttidspunkt, Varighet):
        self.tittel = Tittel
        self.sted = Sted
        self.starttidspunkt = Starttidspunkt
        self.varighet = Varighet

    def __str__(self):
        return f"{self.tittel} \n{self.sted} \nStart dato: {self.starttidspunkt} \nVarer i {self.varighet} minutter"




def Inp():
    try:
        Tittel = input("Tittel av avtalen:")
        if not Tittel.isalpha():
            print("Prøv på nytt")
            Inp()
        Sted = input("Avtale Sted:")
        if not Sted.isalpha():
            print("Prøv på nytt")
            Inp()
        Tid = datetime.datetime(int(input("Starttidspunkt år:")), int(input("Måned:")), int(input("Dag:")), int(input("Timer:")), int(input("Minutter:")), int(input("Sekunder:")))
        Varighet = int(input("Varighet av avtalen:"))
        avtale = Avtale(Tittel, Sted, Tid, Varighet)
        Gruppe.update({Tittel : avtale})
        return avtale
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
                print('faen')
                avtallle = Avtale(u[0], u[1], u[2], u[3])
                gruppe.update(f[1], avtallle)
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

i = 0
Gruppe = {}
while i < 20:
    avtale = Avtale(i, i, i, i)
    Gruppe[i] = avtale
    i += 1
print(Gruppe)




Fil = open("Avtaler.txt", "r")
gruppe = {}

menyvalgRediger()




 
