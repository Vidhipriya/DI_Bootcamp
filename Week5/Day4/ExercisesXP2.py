from operator import iadd


class Currency:
    def __init__(self, currency, amount):
        self.currency = str(currency)
        self.amount = int(amount)
        print(f"{self.currency},{self.amount}")
        
    def __str__(self):
        return f'{self.amount} {self.currency}' 
    def __int__(self):
         return self.amount
    def __repr__(self):
         return f'{self.amount} {self.currency}'
    
    def __add__(self,other):
        if(isinstance(other,int)):
         return self.amount + other
        else:
         return self.amount +other.amount
    
     
     

        
c1=Currency("dollar",5)
c2=Currency("dollar",10)
print(c1+5)

        
     
        
        
        
        
# print(repr(c1))
# print(str(c1))
# print(int(c1))



            
# Currency_depositer.add_currencies("rupees","dollar",10,10)

    # def add_currencies(self,currency1,currency2,amount1,amount2):
    #     self.currency1 = str(currency1)
    #     self.amount1 = int(amount1)
    #     self.currency2 = str(currency2)
    #     self.amount2 = int(amount2)
    #     if currency1==currency2:
    #         add=self.amount1+self.amount2
    #         print(f"{add}")
    #     else:
    #         print(f"TypeError: Cannot add between {self.currency1} and {self.currency2}")