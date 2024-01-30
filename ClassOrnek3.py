class Cizgi:
    def __init__(self, kenar):
        self.kenar = kenar

    def cevre(self):
        return self.kenar

    def alan(self):
        return self.kenar * self.kenar


class Ucgen(Cizgi):
    def __init__(self, __kenar, __yukseklik):
        self.kenar = __kenar
        self.yukseklik = __yukseklik

    def cevre(self):
        return self.kenar * 3

    def alan(self):
        return self.kenar * self.yukseklik / 2


class Dikdortgen(Cizgi):
    def __init__(self, __kenar, __kenar2):
        self.kenar = __kenar
        self.kenar2 = __kenar2

    def cevre(self):
        return (self.kenar2 + self.kenar) * 2

    def alan(self):
        return self.kenar2 * self.kenar
    
class Kare(Cizgi):
    def cevre(self):
        return self.kenar * 4

    def alan(self):
        return self.kenar * self.kenar
    
print(Ucgen(5, 5).cevre())
