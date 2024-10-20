class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Kerros: {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros: {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        while kerros > self.kerros:
            if self.kerros == self.ylin_kerros:
                break
            self.kerros_ylös()
        while kerros < self.kerros:
            if self.kerros == self.alin_kerros:
                break
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissejä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        for i in range(hissejä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)

talo = Talo(0, 10, 3)
talo.aja_hissiä(0, 2)
talo.aja_hissiä(1, 6)
talo.aja_hissiä(2, 3)

talo.palohälytys()