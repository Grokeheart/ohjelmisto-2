class Auto:
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0


auto = Auto("ABC-123", 142)

print(auto.rekisterinumero, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka)