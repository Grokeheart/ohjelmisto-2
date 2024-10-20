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

class Sähköauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisterinumero, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisterinumero, huippunopeus)

sähköauto = Sähköauto("ABC-15", 180, 52.5 )
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3 )

sähköauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(60)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(sähköauto.kuljettu_matka)
print(polttomoottoriauto.kuljettu_matka)