i = 1
while i < 11:
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    no = int(input("No: "))
    vize = int(input("Vize: "))
    final = int(input("Final: "))

    ort = vize * 0.3 + final * 0.7
    
    print(ad, soyad, no, f"ortalama: {ort}")
    i += 1
    if i == 11:
        if input("Çıkmak için E") == "E":
            break