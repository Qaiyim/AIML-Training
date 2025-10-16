def display():
    print('Welcome to recap of function')

def welcome(name):
    print('Welcome to function Mr.\\Ms. ',name)

def cube(num):
    cube_num=num*num*num
    print(f'Cube of given Number: {num} is =\t {cube_num}')

def square(num):
    return num*num

# def salBonus(salary):
#     return salary*0.10
    


# welcome('Qaiyim')
# display()
# my_num=int(input('Enter number to find out Cube:\t'))
# cube(my_num)
# username=input('Enter user name:\t')
# my_num=int(input('Enter number to find out cube and square:\t'))

# welcome(username)
# cube(my_num)
# sq=square(my_num)
# print(f'Square of {my_num} is: {sq}')

#Salary bonus example 1
# my_salary=int(input('Enter salary to find out bonus:\t'))
# bonus=salBonus(my_salary)
# print(f'For salary {my_salary}, Bonus is {bonus}')
# print(f'Salary after bonus:\t',(my_salary+bonus))

#example 2 for salary
def salBonus(salary):
    bonus=salary*0.10
    print(f'Salary {salary} Bonus: {bonus}')

my_salary=float(input('Enter salary to find out bonus:\t'))
salBonus(my_salary)