def function_name(parameters):
    """docstring"""
    """statement(s)"""


def greet(name):
    print("Hello " + name + " have nice day!")


greet("Enes")


def absvalue(num):
    if num >= 0:
        return num
    else:
        return -num


print(absvalue(-5))
print(absvalue(5))
print(absvalue(0))


def myfunc():
    x = 10
    print("value inside myFunc is", x)  # 10


myfunc()
x = 20

print("value outside myFunc is", x)  # 20

"""builtin functions"""
"""user defined functions"""


def greet2(name, msg="good morning"):  # ön tanımlı msg değişkeni
    print("Hello " + name + " " + msg)


greet2("John", "welcome")  # Hello John welcome

greet2("James")  # Hello James good morning


# 1 Positional
# 1 Keyword argument

# Recursion - Recursive Function
def greet3(*names):  # Sayısı belirsiz parametre
    # * = args (arguments)
    # ** = kwargs (Kw arguments) (key & value)
    for name in names:
        print("Hello " + name)


greet3("James", "John", "Vladimir", "Albert")


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = int(input("Enter a number: "))
print(factorial(num))


def double(x):
    return x * 2


print(double(10))
# Lambda
lambdadouble = lambda x: x * 2

print(lambdadouble(10))


def myfunc(x):
    for e in x:
        if e % 2 == 0:
            print(e)


myList = [1, 12, 4, 5, 8, 6, 3, 11]
myfunc(myList)

# Lambda hali
myfuncc = list(filter(lambda x: (x % 2 == 0), myList))

print(myfuncc)

myfunccc = list(map(lambda x: x * 2, myList))

print(myfunccc)


# Global, non-Local, Local variables
# Bir fonksiyonun dışında ya da global alanda tanımlanmış
# değişkenlere Global Değişken denir.
# Bir fonksiyonun içinden ve dışından erişilebilir olan değişkenlerdir.

# Local scopeta ya da bir fonksiyonun içerisinde tanımlanmış olan
# değişkenere Local Değişken denir.

# Non-Local Variable iç içe geçmiş fonksiyonlarda (nested functions)
# kullanılan değişkenlerdir. Local alanda tanımlanmazlar.
# Ne globalde ne de localde bulunurlar. Non-local değişkenleri tanımlamak
# için "nonlocal" keywordü kullanılır.


# x = "Global"


def aFunc():
    global x
    x = "Global"
    print("x inside function", x)


"""
aFunc()

print("x outside function", x)

str = "Global"


def aFunc2(text):
    str = text * 2
    print(str)


aFunc(str)
"""

globalVariable = "Global"


def examplefunc():
    global globalVariable  # bu satır olmazsa bir alt satır çalışmaz!
    globalVariable = globalVariable * 2
    y = "Local"
    print(globalVariable)
    print(y)


examplefunc()
# print(local)

num1 = 5


def globallocal():
    num1 = 10
    print("local number", num1)


globallocal()

print("global number", num1)


def outer():
    x = "local"

    def inner():
        nonlocal x  # bu satır olmazsa nonlocal local yazdırır.
        x = "nonlocal"
        print("inner: ", x)  # "nonlocal"

    inner()
    print("outer: ", x)  # "nonlocal"


outer()

c = 1


def add():
    global c
    c += 2
    print(c)


add()


a = 0
b = "Empty"

# ÇOK ÖNEMLİ!!!
# import edilen dosya hiç kullanılmasa bile içindekiler çalışır!!!

def myfunction():
    a = 20
    def myfunction2():
        a = 25
    print(x)
    myfunction2()
    print(x)

myfunction()
print(a)