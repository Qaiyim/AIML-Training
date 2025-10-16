# num=1
# print("Printing Numbers from 1 to 100")
# while(num<=100):
#     print(num,end=" ")
#     num+=1

#break example
# num=1
# print("Printing Numbers from 1 to 100 before we get the number divisible by 11")
# while(num<=100):
#     if(num%11==0):
#         break
#     print(num,end=" ")
#     num+=1

#continue example
# num=1
# print("Printing Numbers from 1 to 100 those are not divisible by 11")
# while(num<=100):
#      if(num%3==0):
#          num+=1
#          continue
#      print(num,end="\t")
#      num+=1

# num=1
# print("OddNumbers from 1 to 100")
# while(num<=100):
#     if(num%2==0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1

# num=1
# while(num<=100):
#     if(num%5==0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1

# num=1
# print("Printing Numbers from 1 to 100 before we get the number divisible by 2")
# while(num<=100):
#      if(num%5==0):
#          break
#      print(num,end=" ")
#      num+=1

# for i in range(1,100):
#     if(i%4==0):
#         continue
#     print(i,end="\t")


#correctpassword and keep request password if wrong password

correctPwd="Qaiyim@18"
counter=0
while True:
    pwd=input("Please enter password to start the game:\t")
    if(correctPwd==pwd):
        print("Permission Granted")
        print("***Game Started***")
        break
        
    else:
        print("Wrong Password, Try Again")
        counter+=1
        if(counter>=3):
            print("Blocked for further attempt")
            break


