class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp =  hp

    def take_damage(self,amount):
        self.hp -= amount
        pass
    
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(arthur.hp)  # Expected: 90
print(morgana.hp)  # Expected: 100