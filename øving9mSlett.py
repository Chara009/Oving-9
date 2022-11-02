# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:22:59 2022

@author: salim
"""

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
        return avtale
    except ValueError:
        print("Prøv på nytt")
        Inp()

def liste(gruppe, overskrift):
    print(overskrift, "\n")
    for key in gruppe:
        print(key, "\n", gruppe[key], "\n")

def lagring(gruppe):
    file = open("Avtaler.txt", "w")
    for key in gruppe:
        avtalle = gruppe.get(key)
        file.write(f"{avtalle.tittel}; {avtalle.sted}; {avtalle.starttidspunkt}; {avtalle.varighet}\n")
    file.close()

def lesing(liste):
    gruppe = {}
    i = 0
    f = liste.readline()
    while f != "":
        f = f.rstrip("\n")
        f = f.split(";")
        avtale = Avtale(f[0], f[1], f[2], f[3])
        gruppe[i] = avtale
        f = liste.readline()
        i += 1
    return lesing()


        
#m)  Lag et menyvalg for å slette en avtale. Dette menyvalget skal skrive ut avtalelista og deretter 
#la brukeren velge indeksen til avtalen som skal slettes og til slutt slette avtalen. 
'''
def slett_avtale(lesing):
    print(lesing())
    f = input("hvilken avtale vil du slette?")
    for x in lesing:
        if f == 1:
           lesing.remove([lesing[1]])
        if f == 2:
            lesing.remove(lesing[2])
        if f == 3:
           lesing.remove([lesing[3]])
        if f == 4:
            lesing.remove(lesing[4])
   '''     

def menyvalgSlett():
    liste(Gruppe, 'slett')  
    valget = int(input('skriv inn indeksen'))
    Gruppe.pop(valget)
    liste(Gruppe, 'slett')    
    
i = 0
Gruppe = {}
while i < 20:
    avtale = Avtale(i, i, i, i)
    Gruppe[i] = avtale
    i += 1
print(Gruppe)



menyvalgSlett()

        
        
        
        
    
        
        


    
    
    


        
    
    
    
    
            
            
            