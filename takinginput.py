# # username=input("Enter User Name")

# # age=int(input("Enter age"))
# # salary=float(input("Enter Salary"))
# # dataKnw=bool(input("Do You know databases?"))
# # print("Name:",username)
# # print("Your age is ", age)
# # print("Salary is:",salary)
# # print("Know the databases?", dataKnw)

# #Adding Two Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = \t {result}")

# # Multiply Two Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1*num2
# print(f"Result after multiplication {num1} and {num2} = \t {result}")

# # Division Two Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1/num2
# print(f"Result after dividing {num1} by {num2} = \t {result}")

# # % finding reminder example
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1%num2
# print(f"Remainder after dividing {num1} by {num2} = \t {result}")

# Taking more than one input using single line
num1,num2=input("Enter two numbers separated by space").split()
result=int(num1)+int(num2)
print(f"Numbers entered by you are {num1} and {num2} and addition of numbers {result}")