# subjects=("Python","Java","Dotnet","SQL","PowerBI")
# print("All subjects are:\n")
# for sub in subjects:
#     print(sub,end="\t")

# print("\nNumber of subjects are: ",len(subjects))


#tupleName.index(item) will return the index of first occurence of item in tupleName
# numbers=(1,2,3,4,10,45,65,76,34,56)
# for numb in numbers:
#     print(numb)

# search_num=int(input("Enter Number to find out index:\t"))
# if search_num in numbers:
#     print(f"Index of {search_num} is:\t",numbers.index(search_num))
# else:
#     print(f"No such number {search_num} in our tuple")

#Tuple to find multiple times items
# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print("All Numbers in tuple:",len(numbers))
# for num in numbers:
#     print(num)
# search_num=int(input("Enter Number to find out frequency:\t"))
# if search_num in numbers:
#     print(f"Number: {search_num} occurs: {numbers.count(search_num)} times")
# else:
#     print(f"No such number {search_num} in our tuple")


# #Write a program to sum a list with 4 numbers.
numbers=[10,20,30,50]
total=sum(numbers)
print("Sum of numbers is: ",total)

# #Write a program to sum a tuple with 4 numbers.
numbers=(10,20,30,50)
total=sum(numbers)
print("Sum of numbers from tuple is: ",total)
