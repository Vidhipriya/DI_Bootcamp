class Family():
    def __init__(self,members, last_name):
        self.members=members
        self.last_name=last_name
        members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
     ]
    def born(self,**members):
        members.append(self.child)
        print("Congratulations on the baby!")
    def is_18(self,members,age):
        self.age=age
        if self.age>18:
            return True
        else:
            return False
    def family_presentation ():
        print(f"{self.last_name}{self.name}")     
Family("minou","lola")
        