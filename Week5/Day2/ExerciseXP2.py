from ExerciseXP import Dog

class PetDog(Dog):
    def __init__(self,trained):
        self.trained=trained
        trained=False
    def train(self):
        print(f"{self.bark}")
        self.trained=True
    def play(self,*Dog):
        print(f"{self.dog_name} all play together")
    
    def do_a_trick(self):
        if self.trained==True:
            dog_sentences=[f"{self.dog_name} does a barrel roll",f"{self.dog_name} stands on his back legs",f"{self.dog_name} shakes your hand",f"{self.dog_name} plays dead"]
            print(dog_sentences.shuffle())
           