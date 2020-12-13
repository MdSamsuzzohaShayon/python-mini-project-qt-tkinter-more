# Inheritance
# a language feature would not be worthy of the name “class” without supporting inheritance.

# ALL ANIMAL IS NOT CAWS
class Animal:
    def __init__(self):
        self.life = True
        print("This is from super class Animal")

    def eat(self):
        print("All Animal do eat.")


# CAWS IS AN ANIMAL
class Caws(Animal):
    # ALL PROPERTIES AND METHODS OR ANIMAL CLASS ARE AVAILABLE IN HERE
    def __init__(self):
        self.legs_count = 4
        print("This is sub class Caws")

    def can_swim(self):
        print("Caws can swim.")



# MAKING INSTANCE  OR OBJECT
anml = Animal()
print("Animal has life? ",anml.life)
anml.eat()


print("------------")

caw_animal = Caws()
# POLYMORCISM
caw_animal.eat()
print(f"Cow has all {caw_animal.legs_count} legs" )
caw_animal.can_swim()
