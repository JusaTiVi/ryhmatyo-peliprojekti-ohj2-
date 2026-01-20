import random
tiedosto = "sanat.txt"
pistelista = "pisteet.txt"
class Hirsipuu:
    def __init__(self, tiedosto):
        self.tiedosto = tiedosto
        self.nimi = nimi
        self.pisteet = 0
        self.uusi_peli()
    
    def uusi_peli(self):
        self.sana = self.arpa()
        self.vaarat = 0
        self.oikeat = []
        self.kirjaimet = list(set(self.sana))
        self.max_vaarat = 8

    def arpa(self):
        with open(self.tiedosto) as file:
            sanat = file.read().split()
        sana = random.choice(sanat)
        return sana

    def kysy_kirjain(self):
        return input("Anna kirjain: ").lower()

    def tarkista_kirjain(self, kirjain):
        if kirjain not in self.sana:
            self.vaarat += 1
        else:
            if kirjain not in self.oikeat:
                self.oikeat.append(kirjain)
            else:
                return print("kirjain on jo löydetty!")

    def tarkista_havio(self):
        if self.vaarat >= self.max_vaarat:
            print("Hävisit pelin!")
            print("sana oli:", self.sana)
            return True
        return False

    def tarkista_voitto(self):
        if len(self.oikeat) == len(self.kirjaimet):
            print("Voitit pelin!")
            self.pisteet += 1
            self.t
            return True
        return False
    def tallenna_pisteet(self):
        with open(pistelista) as tiedosto:
            tiedosto.write(f"{self.nimi}: {self.pisteet}\n")

    def pelaa(self):
        while True:
            kirjain = self.kysy_kirjain()
            self.tarkista_kirjain(kirjain)

            if self.tarkista_havio():
                break
            if self.tarkista_voitto():
                break
nimi = input("Anna pelaajan nimi: ")
peli = Hirsipuu(tiedosto, nimi)

while True:
    peli.pelaa()
    peli.uusi_peli()