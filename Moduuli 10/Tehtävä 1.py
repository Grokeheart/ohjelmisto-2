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

hissi = Hissi(0, 10)
hissi.siirry_kerrokseen(11)
hissi.siirry_kerrokseen(-1)
hissi.siirry_kerrokseen(10)
hissi.siirry_kerrokseen(0)
