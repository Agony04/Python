'''
    dir(list):
    ['__add__', '__class__', '__class_getitem__', 
    '__contains__', '__delattr__', '__delitem__', 
    '__dir__', '__doc__', '__eq__', '__format__', 
    '__ge__', '__getattribute__', '__getitem__', 
    '__getstate__', '__gt__', '__hash__', 
    '__iadd__', '__imul__', '__init__', 
    '__init_subclass__', '__iter__', 
    '__le__', '__len__', '__lt__', 
    '__mul__', '__ne__', '__new__', 
    '__reduce__', '__reduce_ex__', '__repr__', 
    '__reversed__', '__rmul__', '__setattr__', 
    '__setitem__', '__sizeof__', '__str__', 
    '__subclasshook__', 'append', 'clear', 
    'copy', 'count', 'extend', 'index', 
    'insert', 'pop', 'remove', 'reverse', 'sort']
'''

liste = []

# print(help(liste))
# print(dir(liste))

list(range(10))

liste1 = [0,1,2,3,4,5,6,7,8,9]
liste2 = ["ali", "ramazan", "saban", 10, 20, 30, 40,
          [1,2,3], liste1]

print(liste2[3])            # 10
print(liste2[-1])           # - sağdan başlar ([1,2,3])
print(liste2[0:-1])         # aralık belirtiyor
print(liste2[0:-1:2])       # aralıkta ikişer gidiyor
print(liste2[::2])          # tüm listede ikişer gidiyor

isimler1 = ["recep", "şaban", "ramazan"]
isimler1.append("kazim")
print(isimler1)

isimler2 = ["safiye", "ayla", "gülcan"]
isimler1.append(isimler2) # doğrudan array olarak ekler
print(isimler1)
# ['recep', 'şaban', 'ramazan', 'kazim', ['safiye', 'ayla', 'gülcan']]

isimler1.extend(isimler2) # arraydeki elemanların kendisini ekler
print(isimler1)
# ['recep', 'şaban', 'ramazan', 'kazim', ['safiye', 'ayla', 'gülcan'], 'safiye', 'ayla', 'gülcan']

a = [1,2]
b = [3,4]

# a += b
# print(a)
# [1, 2, 3, 4] (+ operatörü extend yapar)

a[len(a):] = b
print(a)
# [1, 2, 3, 4] (bu işlem de extend yapar)

a1 = [1,2]
a2 = [1,2]

a1.extend(b)
print(a1)
# [1, 2, 3, 4]

a2.append(b)
print(a2)
# [1, 2, [3, 4]]

harfler = ["a", "b", "d", "e"]
harfler.insert(2, "c") # instert(index, object) belirtilen indexe elemanı atıyor
print(harfler)

harfler.remove("e") # bunu açıklamama gerek yok herhalde
print(harfler)

harfler1 = ["a", "b", "d", "e", "e", "e"]
harfler1.remove("e") # böyle bir durumda en küçük indexli olanı siler
print(harfler1)

# harfler1.remove("j") # listede yok, hata döner
print(harfler1)

harfler1.pop(3) # indexine göre siler
print(harfler1) # (yukarıda bir kere e silindi şimdi de silindi bu yüzden bir tane e kaldı)

harfler1.pop(-1) # son elemanı siler
print(harfler1)

#pop()'ta aralık seçeneği yok.

harfler2 = ["a", "b", "c", "d", "e", "e"]
# harfler2.clear()          # Listeyi boşaltır. del harfler2[:] 'de aynısı yapar.
# print(harfler2)           # []
# del harfler2              # Listeyi bellekten siler
# print(harfler2)           # harfler2 is not defined
# del harfler2[:2]
# print(harfler2)           # ["d", "e"]

harfler2.index("e")         # e elemanının indexini döner (birden fazla aynı eleman varsa en küçük olanı döner)
z = harfler2.index("e", 4)  # index(object, starting index)
print(z)

harfler3 = ["a", "c", "d", "e", "e", "e"]
x = harfler3.count("e")     # elemandan kaç tane olduğunu döner
print(x)                    # 3

harfler3.sort()             # Küçükten büyüğe
print(harfler3)

harfler3.sort(reverse=True) # Büyükten küçüğe
print(harfler3)

harfler4 = ["a", "b", "c", "d", "e", "f"]
harfler4.reverse()
print(harfler4)

eski_harfler = ["a", "b", "c", "d", "e", "f"] 
yeni_harfler = eski_harfler # Shallow copy (aynı referansa baktığı için değişikliklere duyarlıdır)

yeni_harfler.append("z")

print(yeni_harfler)
print(eski_harfler)

eski_harfler_copy = ["a", "b", "c", "d", "e", "f"]

yeni_harfler_copy = eski_harfler_copy.copy() # Deep copy (referansları farklı, değişikliklerden etkilenmez)

yeni_harfler.append("y") # Deep copy yapıldığından değişiklik yakalanmaz
print(eski_harfler_copy)
print(yeni_harfler_copy)

harfler5 = ["a", "b", "c", "d", "e"]

# Tuples (Demeletler)
liste = []
demet = () # Tuples sonradan değiştirilemez arraylerdir

denemeDemeti = ("Merhaba", 3, 3.14)
print(type(liste)) # list
print(type(denemeDemeti)) # tuple

demet2 = "Merhaba", 1, 3, 9, "Ali", [8, 9]
print(type(demet2)) # tuple (tuple parantezsiz de tanımlanabilir)

# a, b, c, d, e = demet2
# print(c)

demet3 = ("Merhaba")    # String
demet4 = ("Merhaba",)   # Tuple
demet4 = "Merhaba",     # Tuple

print(demet2[2])        # Tuple[index] şeklinde elemanlara ulaşılır
print(demet2[-1])

# demet2[2] = "a"       # Tuple object doesn't support item assigment

demet2[5][1] = 10       # Tuple içindeki array değiştirilebilir (mutable)
print(demet2[5])

print((1,2,3) + (4,5,6)) # Tuple olarak algılar

print(("Tekrar",) * 3)

print(demet2.count(2))   # Demet2'de hiç 2 olmadığından 0 döner
print(demet2.index(3))   # 3'ün indexini döner

demet5 = ("a", "b", "c", "d")
print("b" not in demet2) # True

liste3 = ["a", "b", "c", "d", "e"]
demet6 = tuple(liste3) # Liste3'ü tuplea dönüştürdü
print(type(demet6))