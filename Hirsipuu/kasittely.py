import random
tiedosto = "sanat.txt"
class Hirsipuu:
    def __init__(self, tiedosto):
        self.tiedosto = tiedosto
        self.sana = self.arpa()
        self.vaarat = 0
        self.oikeat = []
        self.kirjaimet = list(set(self.sana))
        self.max_vaarat = 8

    def arpa(self):
        with open(self.tiedosto) as file:
            sanat = file.read().split()
        return random.choice(sanat)

    def kysy_kirjain(self):
        return input("Anna kirjain: ")

    def tarkista_kirjain(self, kirjain):
        if kirjain not in self.sana:
            self.vaarat += 1
        else:
            if kirjain not in self.oikeat:
                self.oikeat.append(kirjain)

    def tarkista_havio(self):
        if self.vaarat >= self.max_vaarat:
            print("Hävisit pelin!")
            return True
        return False

    def tarkista_voitto(self):
        if len(self.oikeat) == len(self.kirjaimet):
            print("Voitit pelin!")
            return True
        return False

    def pelaa(self):
        while True:
            kirjain = self.kysy_kirjain()
            self.tarkista_kirjain(kirjain)

            if self.tarkista_havio():
                break
            if self.tarkista_voitto():
                break
            
peli = Hirsipuu(tiedosto)
peli.pelaa()