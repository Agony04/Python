class Bird:
    def __init__(self):
        print("Bird class init")

    def fly(self):
        print("Bird is flying")

    def eat(self):
        print("Bird is eating")

    def walk(self):
        print("Bird is walking")

class Parrot(Bird): #Inheritance from Bird
    def __init__(self):
        print("Parrot class init")
        super().__init__()

    def speak(self):
        print("Parrot is speaking")

obj = Parrot()
obj.speak()
obj.fly()