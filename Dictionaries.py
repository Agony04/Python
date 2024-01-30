my_dict = {}
print(type({}))
print(type(my_dict))
print(dir({}))
'''print(help({}))'''

# my_dict = {1: 'apple',
#            2: 'ball'}

# my_dict = {'name': 'Ahmet', 1: [2,3,4]}
# my_dict = dict([(1, 'apple'), (2, 'Bali')])

my_dict = dict({'name': 'Elton John', 'age': 22})

'''
'clear', 'copy', 'fromkeys', 
'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values'
'''

print(my_dict['name'])      # Elton John
print(my_dict.get('name'))  # Elton John, .get(key) returns value of key
print(my_dict.get('yas'))   # None

print(my_dict['age'])       # 22

my_dict['age'] = 27
print(my_dict['age'])       # 27

my_dict['address'] = 'Edirne' # Adding to dictionary
print(my_dict)



squares = {1:1, 2:4, 3:9, 4:16, 5:25}

squares.pop(4) # .pop(key) Deleting key & value from dictionary
print(squares)

squares.popitem() # Deleting last key & value
print(squares)


squares.clear() # Deleting all of elements from dictionary
print(squares) # {}

# del squares # Removing dictionary from memory
# print(squares) # squares is not defined

arrayToDict = {}.fromkeys(['BST207', 'BST209', 'BST202'], 'value')
print(arrayToDict)

for item in arrayToDict.items():
    print(item)

print(list(sorted(arrayToDict.keys()))) # Sorting dictionary keys
print(list(sorted(arrayToDict.values()))) # Soritng dictionary values

myList = {x: x*x for x in range(11) if x % 2 == 1} # Lambda (Tek satırlık metod)
print(myList) # {1: 1, 3: 9, 5: 25}
print(3 in myList) # True
print(25 in myList) # False çünkü defaultta sadece keylere bakıyor
print(25 in myList.values()) # True

print(all(myList)) # Tanımlıysa True döndürür
print(any(myList)) # Boş değilse True döndürür
print(len(myList)) # Uzunluğu döndürür
print(sorted(myList)) # Sorting keys
print(sorted(myList.values())) # Sorting values
print(myList.clear()) # None, Clear parametre almaz ve none döner (no argument)

namelessList = {1:1,2:4,3:9,4:16,5:25}

# new_list = namelessList # Birbirine bağlı, sadece referans atadı.
# new_list.clear()
# print(new_list) # {}
# print(namelessList) # {}

new_list = namelessList.copy() # Harbi kopyalama, referans değil.
new_list.clear()
print(new_list)
print(namelessList)

keys = {'a', 'b', 'c', 'd', 'e'}
values = ['New']
values.append('2')
a = dict.fromkeys(keys, values)
print(a)

listem = {'name': 'Ahmet', 'age': 22}
salary = listem.setdefault('salary', 3000) # Listede yoksa atıyor
age = listem.setdefault('age', 25) # Listede varsa hiçbir şey yapmıyor age 22 kaldı
province = listem.setdefault('province', 'Edirne')
print(listem)
print(salary)
print(age)
print(province)
print(listem)

tekKareler = {x: x*x for x in range(11) if x % 2 == 1}
toplamlar = {x: x+x for x in range(100, 110, 2)}

print(tekKareler)
print(toplamlar)

toplamlar.update(tekKareler) # Sonuna ekliyor
print(toplamlar)

toplamlar.update(name = 'Ahmet', age = 22)
print(toplamlar)