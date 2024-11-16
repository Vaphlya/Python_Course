class Animal :
    def __init__(self, name, species, age) :
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self) :
        if self.species == "Dog" :
            print("GAV")
        if self.species == "Cat" :
            print("Meow")

animal1 = Animal("Barsik", "Cat", 12)
animal2 = Animal("Sobak","Dog", 2)

print(animal1.make_sound())
print(animal2.make_sound())


class Rectangle :
    def __init__(self, widht, height) :
        self.widht = widht
        self.height = height
    
    def calculate_area(self) :
        area = self.widht * self.height
        return area
    
obj1 = Rectangle(22,8)
obj2 = Rectangle(33,12)

print(obj1.calculate_area())
print(obj2.calculate_area())