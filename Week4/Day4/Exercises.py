# Exercise1
# def calculation(num1,num2):
#     sum=num1+num2
#     sub=num1-num2
#     return(sum,sub)

# calculated=calculation(5,2)
# print(calculated)



# Exercise2
def is_less_than_four(s):
    return s[0] == len(people)<=4

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_object = filter(is_less_than_four, people)

map_object = map(is_less_than_four, people)

print(list(map_object))
