# Example 1
# class Emp:
#     def display(self):
#         print('Display of Employee Class')

# obj = Emp()
# obj.display()

#class className:
    #definition of class
    #attribute Method, constructors

#objectName=ClassName()
#objectName.MethodName()

# e=Emp()
# e.display()

#Example 2
class Emp:
    def reg (self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print('Employee details as follows')
        print('Employee ID:\t',self.eid)
        print('Employee Name:\t',self.ename)

e1=Emp()
e2=Emp()
e3=Emp()
e1.reg(1,'Ahmad')
e2.reg(102,'Qaiyim')
e3.reg(109,'Intan')
print('\nFirst Employee Details')
e1.display()
print('\nSecond Employee Details')
e2.display()
print('\nThird Employee Details')
e3.display()
