# import math
# import random
# my_num=int(input('Enter number to find out square root:\t'))
# print(f'Square root of {my_num} is:\t',math.sqrt(my_num))

# print('Your lucky number from1 to 100 is: ',random.randint(1,100))

#To check function inside module
import math
import inspect

# functions=inspect.getmembers(math,inspect.isbuiltin)
# print(functions)

# for n,func in functions:
#     print(n)

print('Sin 90 is: ',math.sin(90))
print('Tan 90 is: ',math.tan(90))
print('Cos 90 is: ',math.cos(90))

deg=int(input('Enter degree to find out cos: '))
print(f'Cos of {deg} is: ',math.cos(deg))
