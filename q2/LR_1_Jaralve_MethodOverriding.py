class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")

    def make_sound(self):
        print(self.name, "makes a sound.")


class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")
    def eat(self):
        print(self.name, "eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets!")
    def eat(self):
        print(self.name, "eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters!")
    def eat(self):
        print(self.name, "eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("------")

elephant.make_sound()
elephant.eat()
print("------")

monkey.make_sound()
monkey.eat()
print("------")
