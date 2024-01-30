# Overload

class P:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return P(x,y)

p1 = P(2,3)
p2 = P(5,6)
print(p1 + p2) # p1.__add__(p2) veya P.__add__(p1, p2)

# sayi1 + sayi2 => sayi1.__add__(sayi2) #Overload
# sayi1 ** sayi2 => sayi1.__pow__(sayi2) #Overload
