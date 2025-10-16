#First way
# from ourpack import welcome
# print(welcome.display())

#Second way
# from ourpack import welcome
# username=input('Please enter your name: ')
# welcome.display(username)

#Third way
from ourpack import welcome
username=input('Please enter your name: ')
msg=welcome.display(username)
print('Message for you: ',msg)


#Class example
# from ourpack import student
# s1=student.Student(1,'Qaiyim')
# s1.display_info()