import sqlite3 as db
class deneme:
    def __init__(self):
        try:
            self.baglan=db.connect("test.db")
        except db.OperationalError:
            exit(1)
        self.imlec=self.baglan.cursor()
    def Veritabaniyarat(self):
        #OUTOINC ID 
        self.imlec.execute('CREATE TABLE İF NOT EXISTS ogrenci \
            (id INT PRIMARKEY,\
             isim CHAR (50,\
             soyisim CHAR(50),\
             numara INT))')
    def kayıtekle(self):
        pgr=[
            (100,"ahmet","mehmet",23543),
            (101,"mehmet","ahmet",29033),
            (102,"selim","genc",98869)
        ]
        self.imlec.executemany("İNSERT İN TO ogrenci \
            (id.isim,soyisim,numara) \
            VALUES (?,?,?,?)",ogr)

        isim=input("isim giriniz :")
        soyisim=input("soyisim giriniz :")
        numara=input("numara griniz :")
        self.imlecexecute("INSERT IN TO ogrenci \
                         VALUES(?,?,?,?)",(id,isim,soyisim,numara))
    def kayitcek(self):
        #WHERE CLOUSE KOYULACAK 
        print("kayıtlar yazdırılıyor.")
        self.imlec.execute('SELECT*FROM ogrenci')
        yazdir=self.imlec.fetchall()
        print(yazdir)
    def veritabanikapat(self):
        self.baglan.commit()
        self.baglan.close()