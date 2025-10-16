#Example in set
# print("Sets in Python")
# set_one={'laptop','earphone','ipad','mobile','headphone','laptop','ipad'}
# print('Number of items in set one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

# #clear(): Remove all the items from set
# set_one.clear()
# print("After clear number of items in set_one are: ", len(set_one))
# for item in set_one:
#     print(item,end=" ")


# set_one={'laptop','earphone','mobile','headphone','ipad'}
# print('Number of items in set one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

# # set_one.remove('headphone')
# set_one.remove('headphone')
# print('\nAfter remove one item from set_one: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")

#union,intersection,difference
# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}

# #union
# #s1.union(s2): Returns a new set with all items from both set s1,s2
# print(f"set_one contains: {len(set_one)} items")
# print(set_one)
# print(f"set_two contains: {len(set_two)} items")
# print(set_two)
# unionset=set_one.union(set_two)
# print(f"Union of set_one and set_two contains: {len(unionset)} following items")

#intersection
#s1.intersection(s2): Returns a new set with all items from both set s1,s2
# set_one={100,200,300,500,700,900,150}
# set_two={50,150,200,700,550,650}

# print(f"set_one contains: {len(set_one)} items")
# print(set_one)
# print(f"set_two contains: {len(set_two)} items")
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f"Intersection of set_one and set_two contains: {len(newset)} following items")
# print(newset)

#difference between set
set_one={100,200,300,500,700,900,150}
set_two={50,150,200,700,550,650}

print(f"set_one contains: {len(set_one)} items")
print(set_one)
print(f"set_two contains: {len(set_two)} items")
print(set_two)
newset=set_one.intersection(set_two)
print(f"Difference of set_one and set_two contains: {len(newset)} following items")
print(newset)


