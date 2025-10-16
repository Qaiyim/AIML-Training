# Example 1
# class Player:
#     def _init_(self):
#         print('Welcome to player class')
    
#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f'Id:{self.id}\t Name:{self.name}\t Team:{self.team}')

# #object creation
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,'Qaiyim','Malaysia')
# p2.reg(32,'Ahmad','Malaysia')
# p3.reg(42,'Intan','China')

# p1.display()
# p2.display()
# p3.display()

# Parameter constructor example 2 and example 3
class Player:   
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'Id:{self.id}\t Name:{self.name}\t Team:{self.team}')

#Example 3
    def __str__(self):
        return f'{self.id} {self.name} {self.team}'

#object creation
p1=Player(69,'Qaiyim','Malaysia')
p2=Player(32,'Ahmad','Palestine')
p3=Player(2,'Intan','China')

# p1.display()
# p2.display()
# p3.display()

print(p1)
print(p2)
print(p3)

