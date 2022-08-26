list_of_numbers=[2,3,1,2,"four",42,1,5,3,"imanumber"]
def addition():
    for i in list_of_numbers:
        try :
            Sum=sum(i)
            print(str(Sum))

        except TypeError:
            print("Looks like there is a string")
    
addition()      
