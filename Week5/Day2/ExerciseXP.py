# Exercise1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# class Siamese(Cat):
#      def sing(self, sounds):
#         return f'{sounds}'

# all_cats=[Bengal,Chartreux,Siamese]

# sara_pets=Pets(all_cats)
# sara_pets.walk()





# Exercise2
class Dog():
    def __init__(self,name,age,weight):
        self.dog_name=name
        self.age=age
        self.weight=weight
    
    def bark(self):
        print(f"{self.dog_name} is barking")
    def run_speed(self):
        run_Speed=self.weight/self.age*10
        print(run_Speed)
        return run_Speed
    def fight(self,other_dog):
        if self.run_speed()*self.weight >other_dog.run_speed()*other_dog.weight :
            print(f"{self.dog_name} has won the fight")
        else:
            print(f"{other_dog.dog_name} has won the fight")

Bulldog=Dog("Jack",3,40)
Rottweiler=Dog("Thomas",4,50)
Sausage_dog=Dog("Richard",8,20)
Bulldog.bark()
Bulldog.fight(Rottweiler)






