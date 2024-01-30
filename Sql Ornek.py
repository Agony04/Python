import sqlite3 as db

class Database:
    def __init__(self):
        try:
            self.baglan = db.connect('test1.db')
        except db.OperationalError:
            print("Veritabanına bağlanılamadı. Lütfen kontrol ediniz.")
            exit(1)
        self.cursor = self.baglan.cursor()
    
    def tabloOlustur(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS ogrenci\
            id INT PRIMARYKEY, \
            isim CHAR(16),\
            soyisim CHAR(16),\
            numara INT PRIMARYKEY')
        
    def kayitEkle(self):
        isim = input("isim: ")
        soyisim = input("soyisim: ")
        numara = int(input("no: "))
        
        self.cursor.execute('INSERT INTO ogrenci (id, isim, soyisim, numara) VALUES(?,?,?)', isim, soyisim, numara)
        
    def ekranaYazdir(self):
        self.cursor.execute('SELECT * FROM ogrenci')
        yazdir = self.cursor.fetchall()
        print(yazdir)
        
    def veritabaniKapat(self):
        self.baglan.commit()
        self.baglan.close()
        
    def kayitGuncelle(self):
        pass
        # UPDATE
    def kayitSil(self):
        pass
        # DELETE
        
# 1- KAYIT EKLE
# 2- KAYIT LİSTELE
# 3- KAYIT GÜNCELLE
# 4- KAYIT SİL
# Arayüzünü yap. (Ana menüye geri dönme seçeneği de olacak)