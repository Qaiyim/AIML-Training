#Example 1
# import math
# num=int(input('Enter number to find out square root: '))
# print(f'Square root of {num}:\t',round(math.sqrt(num),2))


#Example 2 to inspect the module
# import math
# import inspect

# functions=inspect.getmembers(math,inspect.isbuiltin)
# print('All functions in math module')
# for n,func in functions:
#     print(n)

#Example 3 random
# import random
# print('Random number from 1 to 1000')
# print(random.randint(1,1000))

#Example 4
import random
name=input('Enter your name:\t')
luckynumber=random.randint(1,10)
print(f'Welcome Mr.\\Ms. {name} Coupon Number: {luckynumber}')
if(luckynumber==1):
    print(f'Mr.\\Ms. {name} you have won Nissan R35')
elif(luckynumber==3):
    print('You have won a jet to holiday')
elif(luckynumber==39):
    print('You have won a Y15zr')
else:
    print('Better Luck Next Time')
