# from tkinter import Menu
from ExerciseXP import MenuItem


def load_manager():
   client= MenuItem()
    

user=input("MENU\n (a)Add an item\n (d)Delete an item\n (v)View the menu\n (x)Exit\n")
if user=='a':
        def add_item_to_menu():
            name=input("the item's name")
            price=input("the item's price")
            item=MenuItem(name,price)
            if item.save():
                print("Your save request was completed")
            else:
                print("ERROR")
        add_item_to_menu()
elif user=='d':
        def remove_item_from_menu():
            name=input("the item's name \n")
            item=MenuItem.get_by_name(name)
            if item: 
                item_deleted=item.delete()
                if item_deleted:
                  print("Your delete request was completed")
                else:
                    print("ERROR")
            else:
                print("item does not exist")
        remove_item_from_menu()

elif user=='v':      
        def show_restaurant_menu():
           return MenuItem.all()
        show_restaurant_menu()
else:
    pass
        
# load_manager()
# show_user_menu()
# show_restaurant_menu()
# show_user_menu()
    
    