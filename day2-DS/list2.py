# # change the list of item

# containers = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
# new_containers = [container for container in containers if container != 'c4']
# print(new_containers)

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[1]= 20
# print(list)


# #replace the multiple item
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list[1:4] = [20, 30, 40]
# print(list)

# use the map each element in the list

a = [10, 20, 30]
a = list(map(lambda x: x + 1, a))
print(a)

# append the item in the list
a= [10, 20, 30]
b=a.pop(2)  # Remove the first item
print(b)  # Output the removed item
a.append(40)  # Append a new item
print(a)  # Output the modified list

a= [10, 20, 30]
b= [item for item in a if item> 20]
print(b)  # Output the filtered list with items greater than 20

# add item specific index
a = [10, 20, 30]
a.insert(2, 25)  # Insert 25 at index 2
print(a)  # Output the modified list with 25 inserted

# insert element of set of items
list1 = [1, 2, 3]
s= {4,5,6}

list1.insert(3,s)

print(list1)