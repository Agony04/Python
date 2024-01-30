# SET (Küme)
# Unordered
# Unique
# Immutable (can not be changed)

my_set = {1,2,3}
print(type(my_set))

my_set1 = set([1,2,3]) # List to Set
print(type(my_set1))

my_set2 = set((1,2,39)) # Tuple to Set
print(type(my_set2))

liste = ["ahmet", "recep", "saban"]
kume = set(liste)

demet = ("ahmet", "recep", "saban")
kume = set(demet)

metin = "Hello World!"
kume = set(metin)

sayi = 10
# kume = set(sayi) # HATA! Integer sete dönüştürülemez

print(dir(set))

'''
'add', 'clear', 'copy', 
'difference', 'difference_update', 'discard', 
'intersection', 'intersection_update', 'isdisjoint', 
'issubset', 'issuperset', 'pop', 
'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union', 'update'
'''

mySet = {1,2,3,4,5,1,2,3}
print(mySet)                    # {1,2,3,4,5} Tekrar eden elemanlar bir kez yer alır

myList = [1,2,3,4,5,1,2,3]
print(myList)                   # [1,2,3,4,5,1,2,3]
print(set(myList))              # Clears duplicates of Array

a = {}                          # Dictionary
print(type(a))

b = set()
print(b)                        # Set

exampleSet = {1,3,4,5,6}
print(type(exampleSet))         # Set

exampleSet.discard(4)           # 4 elemanını çıkarır (Sette olmayan bir elemanı discard etmeye çalışırsak hata vermez sadece işlem gerçekleşmez)
exampleSet.remove(6)            # 6 elemanını çıkarır (Sette olmayan bir elemanı removelarsak hata verir)
print(exampleSet)

exampleSet2 = set("Hello World")
print(exampleSet2) # {'W', 'e', 'l', 'd', ' ', 'H', 'o', 'r'}

exampleSet2.pop() # Parametre almaz rastgele bir elemanı çıkarır
print(exampleSet2)

exampleSet2.clear()
print(exampleSet2)

# del(exampleSet2)
# print(exampleSet2)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.union(B)                  # Birleşim
print(A|B)                  # Birleşim Shortcut

A.intersection(B)           # Kesişim
print(A&B)                  # Kesişim shortcut

A.difference(B)             # Fark
print(A-B)                  # Fark shortcut

A.symmetric_difference(B)   # Birleşim - Kesişim (Yani ortak elemanları çıkarır)
print(A^B)                  # Birleşim - Kesişim shortcut

print(A.isdisjoint(B))      # Kesişim kümesi YOK mu? (Ortak eleman varsa False)

meyve = set("banana")
print('a' in meyve)         # True
print('a' not in meyve)     # False

for letter in meyve:
    print(letter)

X = frozenset([1,2,3,4])    # Değiştirilemez
Y = frozenset([3,4,5,6])    # Değiştirilemez

print(X.isdisjoint(Y))      # Kesişim kümesi YOK mu? (Ortak eleman varsa False)

# X.add(9)                  # Frozen'a eklenemez
# print(X)





kumem = {1,2,3,4,5}
newKumem = kumem.copy()     # Deep copy
print(newKumem)

kumem.add(6)
print(newKumem)




kume1 = {'a', 'c', 'g', 'd'}
kume2 = {'c', 'f', 'g'}
print(kume1.difference(kume2)) # {'a', 'd'}
print(kume1) # {'a', 'c', 'g', 'd'}
print(kume2) # {'c', 'f', 'g'}

kume1.difference_update(B)
print(kume1) # {'c', 'd', 'g', 'a'}
print(kume2) # {'c', 'f', 'g'}

kume1.intersection_update(B)
print(kume1) # {'c', 'd', 'g', 'a'}
print(kume2) # {'f', 'g', 'c'}

kume3 = {1,2,4,3,5,7}
kume4 = {2,4}

print(kume4.issubset(kume3)) # Parametredeki setin alt kümesi mi?
print(kume4.issuperset(kume3)) # Parametredeki setin üst kümesi mi?
print(kume3.issuperset(kume4)) # Parametredeki setin üst kümesi mi?

print(kume3.symmetric_difference_update(B)) # kume3'ü kume4 ile olan symmetric difference'a dönüştürüyor ("None" return ediyor)
