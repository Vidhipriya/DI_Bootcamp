import random 
def get_words_from_file():
    f=open("sowpods.txt","r+")
    # print(f.readlines())
    f.close()
get_words_from_file()

def get_random_sentence(length):
    f=open("sowpods.txt","r+")
    for i in random.choice( get_words_from_file):
        if f.read()== len():
           print(i)
        else:
            False
    f.close()
get_random_sentence(3)





