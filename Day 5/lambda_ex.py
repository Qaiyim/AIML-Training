# #example 1
# def add(a,b):
#     total=a+b
#     return total

# result=add(12,15)
# print(result)

#Example 2 LAMBDA
# add= lambda a,b:a+b
# multi=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:a-b

# num1=int(input('Enter first number:\t'))
# num2=int(input('Enter second number:\t'))

# print('subtraction result:\t',sub(num1,num2))
# print('Addition result:\t',add(num1,num2))
# print('Multiplication result:\t',multi(num1,num2))
# print('Average result:\t',avg(num1,num2))
# print('Division result:\t',div(num1,num2))

check_odd=lambda n:"Odd Number" if n%2==1 else 'Even Number'
num1=int(input('Enter number to check odd or even:\t'))
print(check_odd(num1))