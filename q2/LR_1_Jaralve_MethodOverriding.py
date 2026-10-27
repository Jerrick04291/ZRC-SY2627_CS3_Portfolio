
# Parent class
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

print(lion.make_sound())
print(lion.eat())
print("------")

print(elephant.make_sound())
print(elephant.eat())
print("------")

print(monkey.make_sound())
print(monkey.eat())
print("------")