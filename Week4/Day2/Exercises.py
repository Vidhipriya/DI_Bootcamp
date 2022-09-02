list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)]=200









a_tuple = (10, 20, 30, 40)
a,b,c,d=a_tuple
print (a)
print (b)
print (c)
print (d)

#Loop1
user=int(input("give me a number"))
numbers=range(1,13)
for number in numbers:
     print(f"{number} x {user_num} = {number* user_num}")
print("\n")

# Loop2
current_number = 1 
while current_number <= 10:    
    print(current_number)   
    current_number += 1

print("Finished")



