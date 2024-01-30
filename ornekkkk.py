my_int = 1
my_str = "Hello"

try:
    result1 = my_int + my_str
    result2 = my_int + my_int
    result3 = my_str + my_str
    print(round('13, 10'))
    print(round(13, 10))
except TypeError:
    print("value error")
finally:
    print("finally")

# ValueError:
# Sayı olmayan bir değerin int() içine alınması

# ZeroDivisionError:
# Sayıyı sıfıra bölmeye çalışırsak

# NameError:
# Değişken tanımlı değilse