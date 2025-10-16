#Filter example 1
# number =[10,25,30,40,2,1]

# print('\nOriginal List\n')
# for num in number:
#     print(num, end=" ")


# even_number=list(filter(lambda n:n%2==0,number))
# print('\nEven Numbers from List as follows\n')
# for num in even_number:
#     print(num, end=' ')

#Example 2 filter
#Write code using filter to find out all the number less than 5 from the list

# number =[4,2,5,6,7,3,1,10]

# print('\nOriginal List\n')
# for num in number:
#     print(num, end=" ")


# our_number=list(filter(lambda n:n<5,number))
# print('\nEven Numbers from List as follows\n')
# for num in our_number:
#     print(num, end=' ')

#Filter example by using dictionary
# students_marks={'Qaiyim':95,
#                 'Fitri': 89,
#                 'Aiman': 79,
#                 'Adib': 80,
#                 'Evelyn':20,
#                 'Wallase': 15
#                 }
# print('All students')
# print(students_marks)
# pass_students=dict(filter(lambda i: i[1]>=50, students_marks.items()))
# print('Passed Student')
# print(pass_students)

#Filter example 2
students_marks={'Qaiyim':95,
                'Fitri': 89,
                'Aiman': 79,
                'Adib': 80,
                'Evelyn':20,
                'Wallase': 15
                }
print('All students')
for k,v in students_marks.items():
    print(f'Name: {k} -> Marks: {v}')

pass_students=dict(filter(lambda i: i[1]>=50, students_marks.items()))
print('\nPassed Student')
print(pass_students)
for k,v in pass_students.items():
    print(f'Name: {k} -> Marks: {v}')

sort_pass_students=dict(sorted(pass_students.items(), key=lambda  i: i[1]))
print('\nAscending Order')
for k,v in sort_pass_students.items():
    print(f'Name: {k} -> Marks: {v}')

sort_pass_students_desc=dict(sorted(pass_students.items(), key=lambda  i: i[1],reverse=True))
print('\nDescending Order')
for k,v in sort_pass_students_desc.items():
    print(f'Name: {k} -> Marks: {v}')
