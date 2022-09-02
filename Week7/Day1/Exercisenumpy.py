import numpy 

def numpy_id_array(user):
    user=input("put a id array here")
    user= user.split(",",user)
    user=list(map(int,user))
    user=numpy.array(user)
    return f"The minimum value in the array is {numpy.min(user)}\n subtraction by {user-4} \nThe standard deviation of the data {numpy.std(user)}\n The product of the elements in the array {numpy.dot(user,user)}\n"
print(numpy_id_array())