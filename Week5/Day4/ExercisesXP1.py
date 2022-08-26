from msilib import CAB


class Calculator():
    """Finds whether a value is an absolute or integer and allows one to input"""
 
    def absolutes(self,value):
        self.value=value
        print(abs(value))
        
    def integers(self,value):  
        self.value=value
        print(int(value))
        
    def inputter(self,value):  
        self.value=value
        print(input(str(value)))
print(Calculator.__doc__)
Calculatorer=Calculator()
Calculatorer.inputter("can you do this for me")
