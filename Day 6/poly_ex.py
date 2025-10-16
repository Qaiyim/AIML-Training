# class Bird:
#     def fly(self):
#         print('Bird can fly')

# class Airplane(Bird):
#     def fly(self):
#         print('Airplane can fly')

# b=Bird()
# print('Bird Implement')
# b.fly()

# print('Airplane Implementation')
# a=Airplane()
# a.fly()

# print('Using for loop')
# for obj in [Bird(),Airplane()]:
#     obj.fly()


# Example 2
# class Emp:
#     def reg(self):
#         self.id=int(input('Enter Id:\t'))
#         self.name=input('Enter Name:\t')


#     def display(self):
#         print('Name: ',self.name)
#         print('Id:\t',self.id)

# class Dev(Emp):
#     def reg(self):
#         super().reg()
#         self.domain=input('Enter Domain:\t')

#     def display(self):
#         super().display()
#         print('Domain:\t',self.domain)

# d1=Dev()
# d1.reg()
# d1.display()


#example 3 tutorial
class Emp:
    def __init__(self,id,name,qualification):
        self.id=id
        self.name=name
        self.name=name
        self.qualification=qualification
    
    def display(self):
        print('ID:\t',self.id)
        print('Name:\t',self.name)
        print('Qualification:\t',self.qualification)

class Dev(Emp):
    def __init__(self, id, name, qualification,project,domain):
        super().__init__(id, name, qualification)
        self.project=project
        self.domain=domain

    def display(self):
        super().display()
        print('Project:\t',self.project)
        print('Domain:\t',self.domain)

#create one Emp with id=1, name='Qaiyim',qualification='ACCA'
emp=Emp(1,'Qaiyim','ACCA')
#create one Dev with id=3, name='Intan',qualification='Media',project='eShopping', Domain='dot net'
dev=Dev(3,'Intan','Media','eShopping','dotnet')
#Display Dev details
print('Developer details as follows')
dev.display()
#Display Emp details
print('Employee details as follows')
emp.display()


