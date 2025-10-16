#default parameter in functions
# def info(id,name,city='KL'):
#     print(f'Details asa follows \n ID: {id} Name: {name} City:{city}')

# info(1,'Qaiyim','Merbok')
# info(103,'Intan')
# info(103,'Ahmad')

#Tutorial create method that can be able to add 2 numbers, 3 numbers, 4 numbers 
#and return correct total

# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5

# print('Result: ',add(1,2))
# print('Result: ',add(1,2,5,8,3))
# print('Result: ',add(10,23,12))

# def add(*nums):
#     return sum(nums)

# print('Sum of 1,10,11 is:\t',add(1,10,11))
# print('Sum of 5,2 is:\t', add(5,2))
# print('Sum of 10,30,40 is:\t', add(10,30,40))


#Maximum example
def findMax(*nums):
    return max(nums)

print('Maximum of 1,10,11 is:\t',findMax(1,10,11))
print('Maximum of 5,2 is:\t', findMax(5,2))
print('MAximum of 10,30,40 is:\t', findMax(10,30,40))

#Minimum example
def findMin(*nums):
    return min(nums)

print('Minimum of 1,10,11 is:\t',findMin(1,10,11))
print('Minimum of 5,2 is:\t', findMin(5,2))
print('Minimum of 10,30,40 is:\t',findMin(10,30,40))

