import random 
def math():
    user=input("Give me a number between 1 and 100 :\n")
    rando= random.random() * 100
    if rando==user:
        print("You chose the same number as the computer YAYY!")
    else:
        print("Try again")
math()