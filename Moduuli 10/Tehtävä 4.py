import random

class Auto:
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        nopeus = nopeuden_muutos + self.nopeus
        if nopeus > self.huippunopeus:
            nopeus = self.huippunopeus
        if nopeus < 0:
            nopeus = 0
        self.nopeus = nopeus

    def kulje(self, tunteja):
        self.kuljettu_matka += self.nopeus * tunteja

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        autot.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)
        print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
        for auto in autot:
            print(f"{auto.rekisterinumero} | {auto.huippunopeus} | {auto.nopeus} | {auto.kuljettu_matka}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka > self.pituus:
                return True
            else: return False

autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja_kulunut = 0

while True:
    kilpailu.tunti_kuluu()
    tunteja_kulunut += 1
    print(f"Tunteja kulunut: {tunteja_kulunut}")

    if tunteja_kulunut % 10 == 0:
        kilpailu.tulosta_tilanne()

    if kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
        break
