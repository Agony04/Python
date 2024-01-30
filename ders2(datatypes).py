number = 10
number = 1,1
website = "apple.com"
print(website)
website = "microsoft.com"
print(website)

a,b,c, = 5,3.2,"merhaba"
x = y = z = "merhaba"
print(y)

# Sabitler (Constants) (Bütün harfleri büyük yazilir) 
# (python3'de henüz const yok, göstermelik olmasi için büyük yaziliyor.)
PI = 3.14
GRAVITY = 98
print(PI)
PI = 8.15
print(PI)

# snake_case
# camelCase
# MACRO_CASE (pascalcase)
# CapWords

# Numerik Literaller:
# int, float ve complex
a = 0b1010 # binary 
b = 100 # decimal
c = 0o310 # octal
d = 0x12c # hexadecimal
float1 = 10.5
float2 = 1.5e2

x = 3.14j # complex

strings = "merhaba"
char = "c"
multiline = """Bu çok karakterli bir satirdir"""
unicode = u"\u00ddcc"
rawstring = r"raw\nstring"
x = (1 == True)     # True
y = (1 == False)    # False
a = True + 4        # 5
b = False + 10      # 10

a = 5
print(a, type(a))
b = 2.0
print(b, type(b))
c = 1 + 2j
print(c, type(c))

# Liste (List) (Array)
Liste = []
Liste = [2,5,8,"Ali"]
Liste[:2] # [başlangiç : bitiş]

# Küme (Tuple)
Kume = (1,2,3)

# Obje (Object) !!
set1 = {5,2,3}

# Sözlük (Dictionary) (key & value)
d = {"Ahmet": 5428502910, "Remziye": 5052526119}
print(type(d))

# Conversion between data types
int(10.6)       # float to integer
float(5)        # integer to float
float('2.5')    # string to float
str(25)         # integer to string

set([1,2,3])    # array to object
tuple({1,2,3})  # object to tuple
ln = list('merhaba eray') # string to list (array)
print(ln)

ln2 = set('merhaba eray') # string to object
print(ln2)

# if test_ifadesi:
    # durumlar (statements)

num = -1
name = "Tolga"
if num > 0:
    print(num, "bir pozitif sayidir.")
    if name == "Tolga":
        print("İsmi Tolgadir.")

elif num == 0:
    print(num, "sifirdir.")
else:
    print(num, "bir negatif sayidir.")

print("Bu satir sürekli çalişacak.")

# Nested if (İç içe if)
num = int(input("Bir sayi giriniz.")) # Input default stringtir, inte dönüştürdük

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")