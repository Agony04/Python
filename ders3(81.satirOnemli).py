# for
# syntax:
# for item in sequence (its foreach like)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
sum = 0
for val in numbers:
    sum += val
print(sum)

# range()
# syntax:
# range(start, stop, stepsize)
# list() içine range() koyulunca array çıktı verir.

print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

musics = ['pop', 'rock', 'jazz']
for i in range(len(musics)): # len() = lenght
    print("bu müzik türünü çok severim: ",musics[i])

numbers = [0, 10, 15]
for i in numbers:
    print(i)
else: # for içindeki else ifadesi döngü sonlanınca çalışır.
    print("yazdiracak eleman kalmadi")

soyad = 'Kalem'
notlar = {
    'Ahmet': 90,
    'Recep': 80,
    'Kalem': 70
}
for ogrenci in notlar:
    if ogrenci == soyad:
        print(notlar[ogrenci])
        break # break olduğundan for'un else'ine girmedi.
else:
    print("Yazdirilacak öğrenci bulunamadi")

# while
# syntax:
# while text_expression:
#   body

sayi = int(input("bir sayı giriniz: "))
sum = 0
i = 1

while i <= sayi:
    sum += sayi
    i += 1

print(sum)

count = 0
while count < 3:
    print("Inside loop")
    count = count + 1
else:
    print("Inside else")

'''for var in sequence:
    # Inside for loop
    if condition:
        break # break outside'a götürür
    # Inside for loop
# Outside for loop'''

'''while text_expression:
    # Inside while loop
    if condition:
        break # break outside'a götürür
    # Inside while loop
# Outside while loop'''

for val in "String":
    if val == "i":
        break
    print(val)
print("Işlem bitti")

sequence = {'p','a','s','s'}

for val in sequence:
    pass

def Function(args): # args = parametre sayısı belirsiz
    pass

class Example:
    pass

# __init__ = constructor

# dir()
# parametredeki değişken ile kullanılabilecek tüm fonksiyonları yazar