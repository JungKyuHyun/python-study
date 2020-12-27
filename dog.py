class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('cob', 1)

my_dog.sit()
my_dog.roll_over()
print(my_dog.name)

class DogDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

my_dog2 = DogDog('Cobcob', 20)
my_dog2.sit()
