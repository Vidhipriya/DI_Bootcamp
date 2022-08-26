# # Exercise1

# class Cat():
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# my_cat= Cat(cat_name="minou",cat_age=3)
# neighbour1_cat=Cat(cat_name="milette",cat_age=4)
# neighbour2_cat=Cat(cat_name="boy",cat_age=1)
# cats=[my_cat,neighbour1_cat,neighbour2_cat]
# def oldest():
#     oldest=cats[0]
#     for i in cats:
#         if i.age>oldest.age:
#          oldest=i
        
# print(f"The oldest cat is {oldest.name} and is aged {oldest.age}")
# oldest()



# Exercise2
# class Dog():
#     def __init__(self,name,height) :
#         self.name=name
#         self.height=height
    
#     def bark(self):
#         print(f"{self.name}goes woof!")
    
#     def jump(self):
#         jumpHeight= self.height*2
#         print(f"{self.name} jumps {jumpHeight} cm high")
        
# davids_dog=Dog(name="rex",height=50)
# print(f"{davids_dog}")
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog=Dog(name="Teacup",height=20)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if sarahs_dog.height>davids_dog.height:
#     print(f"Sarahs dog{sarahs_dog.name} is bigger")
# else:
#     print(f"davids dog {davids_dog.name} is bigger")



# Exercise3
# class Song():
#     def __init__(self,lyrics):
#         self.lyrics=lyrics
    
        
#     def sing_me_a_song(self):
#         for i in self.lyrics:
#             print(f"{i}")
    
# stairway= Song(["There's a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# Exercis4
class Zoo():
    def __init__(self,zoo_name) :
       
        self.animals=[]
        self.name=zoo_name
     
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)     
    
    def get_animals(self):
        print(f"{self.animals}")
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        print(f"{self.animals}")
    animal_list={
        a:Ape,
        
    }
        
        
the_zoo = Zoo("zoon")      
the_zoo.add_animal("Ape")
the_zoo.add_animal("Cougar")
the_zoo.add_animal("Bear")
the_zoo.add_animal("Baboon")
the_zoo.add_animal("Eel")
the_zoo.add_animal("Emu")
the_zoo.get_animals()
the_zoo.sort_animals()
        


    
  

