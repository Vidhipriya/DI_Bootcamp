# # Exercise1

# my_fav_numbers=set()
# my_fav_numbers.add(1)
# my_fav_numbers.add(2)
# my_fav_numbers.remove(1)

# friend_fav_numbers=set()
# friend_fav_numbers=7
# # our_fav_number=set
# print({friend_fav_numbers} + {my_fav_numbers})



# # Exercise2
# one_tuple=(1,2,3,4)
# # no



# # Exercise3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")
# basket.insert(0,"Apples")
# basket.count("Apples")
# basket.clear()
# print(basket)


 


# # Exercise6
# user_name=input("Tell me your name")
# my_name=["vidhipriya"]
# while my_name==user_name:
#     print("we have the same name")
#     continue


# Exercise7
# user=str(input("Hey tell me your fav fruit(s) separate the fruits with a single space"))
# user=user.split()
# user2=str(input("Enter your fruit name"))
# if (user2 in user):
#     print("You have chosen one of your favourite fruits")
# else:
#     print("You have chosen a new fruit")





 

# # Exercise8
# while True:
#     pizza = input("What kind pizza topping would you like: ")
#     if pizza == "quit":
#         break
#     print("I will add the {} topping to your pizza".format(pizza))






# Exercise9
total=[]

while True:
    age = input("How old are you? ")
    
    if age == "quit":
        print("your sum is " +str(sum(total)))
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free")
        total.append(0)
    elif age < 12:
        print("Your ticket is $10")
        total.append(10) 
    else:
        print("Your ticket is $15")
        total.append(15)





# Exercise10

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches =[]

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I have made" + current_sandwich)
#     finished_sandwiches.append(current_sandwich)
# print()
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich + " is completed\n")







    
# # Exercise11
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich","Pastrami sandwich"]
# finished_sandwiches =[]

# print("no pastrami...")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print()
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("The sandwich is " + current_sandwich)
#     finished_sandwiches.append(current_sandwich)
# print()
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title() + "completed")