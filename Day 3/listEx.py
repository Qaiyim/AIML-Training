# print("List Example One")

# my_list=[10,20,30,"Python", None, True, 12.45]
# print("Number of items in list are:",len(my_list))
# for item in my_list:
#     print(item)

# print("List Example One")

# my_list=[10,20,30,"Python", None, True, 12.45]
# print("Number of items in list are:",len(my_list))
# for item in my_list:
#     print(item)

#Second example of List
# print("Second Example of List")
# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("All employees")
# print("Number of employees:",len(emps))
# for emp in emps:
#      print(emp)

# #Sort example from list in ascending
# emps.sort()
# print("List after sorting")
# for e in emps:
#     print(e)

#Reverse example
# emps.reverse()
# print("\nEmployees In Descending Order")
# for e in emps:
#     print(e)

#append, remove, pop insert method

# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("Number of employees:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

    #append: adds the item at the end of list
# newEmp=input("\nEnter employee name to add in list:\t")
# emps.append(newEmp)
# print("\nAfter adding New Employee Number of employees are:",len(emps))
# for emp in emps:
#     print(emp)

#insert(index,item): This will add item at given index
# newEmp=input("\nEnter employee name to add in list:\t")
# pos=int(input("Enter position where you want to insert inside list:\t"))
# emps.insert(pos,newEmp)
# print("\nAfter adding New Employee Number of employees are:",len(emps))
# for emp in emps:
#     print(emp)

#Delete
# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("Number of employees:\t",len(emps))
# for emp in emps:
#     print(emp,end=" ")
# delEmp=input("\nEmployee to remove from the list")
# emps.remove(delEmp)
# print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
# for emp in emps:
#     print(emp)

#By using if items is not in the list
# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("Number of employees:\t",len(emps))
# for emp in emps:
#     print(emp,end=" ")
# delEmp=input("\nEmployee to remove from the list")
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employees after deleting {delEmp} in list are:",len(emps))
#     for emp in emps:
#         print(emp)
# else:
#     print(f"No such item {delEmp} in employee list")

#pop () example
#listName.pop(index): will delete element at given index and return its value
# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("Number of employees:\t",len(emps))
# for emp in emps:
#     print(emp,end=" ")
 
# del_index=int(input("\nEnter Index to pop items:\t"))
# print("Pop Result: ",emps.pop(del_index))

# print("Number of employees after pop () are:",len(emps))
# for emp in emps:
#     print(emp)


#find out first and last elemnt from list
# emps=["Fitri","Nazrul","Adib","Qaiyim","Syafiah","Iman","Kimi","Pejal"]
# print("Number of employees:\t",len(emps))
# for emp in emps:
#     print(emp)

# print("\nFirst Element of employees in the list is: ",emps[0])
# print("\nLast Element of employees in the list is: ",emps[7])

