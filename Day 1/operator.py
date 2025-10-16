# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \n Discount: {discount} \n DiscountedPrice:{disPrice}")

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus #salary=salary+bonus
# print("Salary with Bonus",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds #salary=salary+tds
# print("Salary after tax",salary)

# age=int(input("Enter yout age"))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("Sorry!!! You are not eligible")
# print("End of Program")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in Exam")
# else:
#     print("Clear the exam")

# print("End or program")    

#accessCode="wes12"

# accessCode=input("Enter Access Code")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Welcome to your course")

# accessCode=input("Enter Access Code:\t")
# if(accessCode=="wes12"):
#    print("Welcome to your course")
# else:
#     print("Invalid Access Code")



# #Logical operators: and, or, not
# phyMarks=int(input("Enter marks obtained in Physics:\t"))
# cheMarks=int(input("Enter Marks obtained in Chemistry:\t"))
# matMarks=int(input("Enter Marks obtained in Mathematics:\t"))

# if((matMarks>=55) and (phyMarks>=50) and (cheMarks>=60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not got the required marks")


# idProof=input("Enter Id proof you have:\t")
# if((idProof=="passport")or(idProof=="dl")or(idProof=="voter id")):
#     print (f"Valid Id {idProof} we accept here")
# else:
#     print("Only passport.dl and voter id are accepted as Identiry Proof")
#     print(f"{idProof}: is not valid ID here")


# #Logical operators: and, or, not

matMarks=int(input("Enter Marks obtained in Mathematics:\t"))
gapYear=int(input("Enter Year gap if any otherwise zero \t"))
    if((matMarks>=55) and (gapYear!=0)):
     print("Not eligible for Btech")
    else:
     print("Eligible for Btech")