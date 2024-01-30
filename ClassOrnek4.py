class Oyun:
    def __init__(self):
        self.enerji = 150
        self.para = 1000
        self.fabrika = 3
        self.isci = 10
        
    def yazdir(self):
        print("enerji", self.enerji)
        print("para", self.para)
        print("fabrika", self.fabrika)
        print("isci", self.isci)
        
    def fabrikaKur(self, adet):
        if self.enerji >= 40 and self.para >= 100:
            self.fabrika = adet + self.fabrika
            self.enerji = self.enerji - (40 * adet)
            self.para = self.para - (100 * adet)
            print(f"{adet} adet fabrika kuruldu.")
        else:
            print("Enerji ya da para yetersiz.")

game1 = Oyun()

game1.fabrikaKur(100)