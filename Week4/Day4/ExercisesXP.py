# Exercise1
def display_message():
    msg = "I'm learning functions today."
    print(msg)

display_message()

# Exercise2
def favorite_book(title):
    print(title + " is one of my favorite books.")
favorite_book('The importance of being earnest')
print("favorite_book")



# Exercise5
def make_shirt(size, message):
   
    print("\nThe size of the shirt is" + size + " t-shirt.")
    print('and the text is, "' + message + '"')
make_shirt()
make_shirt('large', 'I love Python!')
make_shirt(size='medium')
make_shirt('small', 'I like ice-cream')







# Magicians 
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

def make_great(magicians):
    
    great_magicians = []


    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)
