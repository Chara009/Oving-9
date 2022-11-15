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