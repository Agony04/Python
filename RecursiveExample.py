# def power(num, power):
#     if(power == 0):
#         return 1
#     else:
#         return num * power(num, power - 1)

# # print(power(7, 2))

# num1 = int(input("Enter a number"))
# num2 = int(input("Enter a power"))

# print(power(num1, num2))

num1 = input("bir sayi giriniz")


def tek():
    print("Tek sayi")


def cift():
    print("Cift sayi")


if int(num1) % 2 == 0:
    cift()
else:
    tek()


def selamVer(isim):
    print(f"Merhaba, {isim}")


selamVer("Ahmet")

mylongfloat = 2.348573475
print("sayi: %lf" % mylongfloat)

mychar = 'H'
print("char: %c" % mychar)

myint = 5
print("sayi: %d" % myint)

myfloat = 23.0
print("sayi: %f" % myfloat)  # integer gelirse floata çevirir.

sayilar = [4, 2, 5, 8, 2, 6]


def HepsiniCarp(liste):
    result = 1
    for sayi in liste:
        result *= sayi
    return result


print(HepsiniCarp(sayilar))


def kayitYap(isim, soyisim, sehir, tel, meslek, ilce):
    kayit = {}
    kayit["%s %s" % (isim, soyisim)] = [sehir, tel, meslek, ilce]

    for k, v in kayit.items():
        print(k)
        print("-" * len(k))
        for i in v:
            print(i)


kayitYap("Enes", "PINAR", "Tekirdağ", "5335494159", "Öğrenci", "Süleymanpaşa")

n = int(input("Fibonacci icin sayi giriniz."))


def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))

aylar = ["ocak", "subat", "mart", "mayis", "temmuz", "aralik"]


def filterByM(liste):  # Classic
    for ay in liste:
        if ay[0] == "M":
            print(ay)


print(list(filter(lambda ay: ay[0] == "M", aylar)))  # Lambda

deneme = "şu an dışarıda kar yağıyor"
print(list(map(lambda x: len(x), deneme.split())))


def Hacim(u=1, d=1, y=1):
    return u * d * y


print(Hacim())
print(Hacim(5))
print(Hacim(5, 10))
print(Hacim(5, 10, 7))


def test(arg1, agr2, arg3):
    print(arg1, agr2, arg3)


args = ("iki", 3)
test(1, *args)


def example(*args):
    print(args)


L = [1, 2, 3]
example(*L)

# *args Liste, set ve tuple'larda kullanılabilir.
# **kwargs Dictionaryde kullanılır.

D = {'b': 5, 'c': 7}


def example2(**kwargs):
    print(kwargs)


example2(**D)
