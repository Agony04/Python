while True:
    try:
        num1 = int(input("Birinci sayiyi giriniz"))
        num2 = int(input("İkinci sayiyi giriniz"))
        result = num1 / num2
        print(result)
    except ValueError:
        print("Sayi girmeniz lazim")
    except ZeroDivisionError:
        print("Sence 0'da bölünebilir mi")