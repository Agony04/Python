# Virtual & Override

class Cat:
    def speak(self):
        print("nya")

    def eat(self):
        print("Cat is eating")


class Dog:
    def speak(self):
        print("woof")

    def eat(self):
        print("Dog is eating")


def eat_test(mammal):
    mammal.speak()
    mammal.eat()


obj1 = Cat()
obj2 = Dog()

eat_test(obj1)
eat_test(obj2)