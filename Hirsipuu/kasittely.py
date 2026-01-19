import random
while True:
    with open("sanat.txt") as tiedosto:
        sanat = tiedosto.read().split()
    sana = random.choice(sanat)
    vaarat = []
    oikeat = []
    kirjaimet = []
    yritys = input("Anna kirjain: ")
    vastaus = list(sana)
    vaarat = 0
    if yritys not in vastaus:
        vaarat += 1
    else:
        if yritys not in oikeat:
            oikeat.append(yritys)
    if vaarat == 8:
        print("hävisit pelin!")
        break
    for kirjain in vastaus:
        if kirjain not in kirjaimet:
            kirjaimet.append(kirjain)
    if len(oikeat) == len(kirjaimet):
        print("voitit pelin!")