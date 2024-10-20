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

auto = Auto("ABC-123", 142)
nopeudet = [30, 70, 50, -200]
print(auto.rekisterinumero, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka)

for nopeus in nopeudet:
    auto.kiihdytä(nopeus)
    print(auto.rekisterinumero, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka)
