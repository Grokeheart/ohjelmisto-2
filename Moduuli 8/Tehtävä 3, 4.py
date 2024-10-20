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

autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", random.randint(100, 200)))

kisa_kesken = True
while kisa_kesken:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka > 10000:
            kisa_kesken = False

print("Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka")
autot.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)
for auto in autot:
    print(f"{auto.rekisterinumero} | {auto.huippunopeus} | {auto.nopeus} | {auto.kuljettu_matka}")