Exercise 3 

cars = 100 
# 
space_in_a_car = 4.0
# float
drivers = 30
# integer
passengers = 90
# int
cars_not_driven = cars - drivers
# int
cars_driven = drivers
# int ,has the same value as 
carpool_capacity = cars_driven * space_in_a_car
# float
average_passengers_per_car = passengers / cars_driven
# int
print("There are", cars, "cars available.")
# There are 100 cars available /int
print("There are only", drivers, "drivers available.")
# There are only 30 drivers available/int
print("There will be", cars_not_driven, "empty cars today.")
# There will be 70 empty cars today/int
print("We can transport", carpool_capacity, "people today.")
# We can transport 120.0 people today/float
print("We have", passengers, "to carpool today.")
# WE have 90 passengers to carpool today/int
print("We need to put about", average_passengers_per_car,"in each car.")
# We need to put about/float


Exercise 4
age = input("How old are you? ")
print("You are {} years old".format(age))
# you are age-that-has-been-input years old

Exercise 5
user=input(Give me a number between 1 and 100)3
 if int(user)%3==0:
   print("Frizz")
 elif int(user)%5==0:
	print("Buzz")
 else int(user)%3==0 and int(user)*5==0:
print("FrizzBuzz") 