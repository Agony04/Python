import sqlite3 as db

baglan = db.connect("test.db") # Default Desktop
# baglan = db.connect("c:/users/admin/Desktop/test.db")

imlec = baglan.cursor() # idk wth it is
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci(isim, soyisim, numara)")

# CRUD
imlec.execute("INSERT INTO ogrenci VALUES('Ahmet', 'YILDIZ', 1222606009)")

veriler = [
        ("Mehmet", "YILDIZ", 1222606008),
        ("Gamze", "SAYGI", 1222606006),
        ("Mike", "TYSON", 1222606002),
]

for i in veriler:
    imlec.execute('INSERT INTO ogrenci VALUES(?,?,?)', i)

isim = input("isim giriniz: ")
soyisim = input("soyisim giriniz: ")
numara = int(input("numara giriniz: "))

imlec.execute('INSERT INTO ogrenci VALUES (?,?,?)', (isim, soyisim, numara))

arananisim = input("aranacak ismi giriniz: ")
imlec.execute("SELECT * FROM ogrenci WHERE isim = '%s'" %(arananisim))

baglan.commit()
# imlec.execute("SELECT isim, soyisim FROM ogrenci")

# * tüm fieldları temsil eder (all fields)
imlec.execute("SELECT * FROM ogrenci")

yazdir = imlec.fetchall()
arananiyazdir = imlec.fetchone()
print(yazdir)
if arananiyazdir:
    print(arananiyazdir)
else:
    print("Aranan isim mevcut değil.")
    