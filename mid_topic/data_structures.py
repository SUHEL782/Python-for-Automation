#Data structure list* 

#1. List   
# Why need => this is needs for orginize data to retrive it easily.

requrement = ["milk", "eggs", "bread", "butter"]
#print(requrement)
 # second item in the list
requrement.append("cheese") # add item to the list
#print(requrement)

#print(dir(requrement)) # show all the methods of the list

#Dictionary    Dictionary is a collection of key-value pairs./Distionary is a mutable, unordered collection of items.
# Why need => this is needs for orginize data to retrive it easily.
#Distionary used the device information.

Divice_Info = {
    "brand": "Apple",
    "model": "iPhone 13",
    "year": 2021,
    "color": "black"
}
#print(Divice_Info)
print(Divice_Info["brand"]) # access the value of the key "brand"
Divice_Info.update({"model":"iphone 14"}) # access the value of the key "model"

print (Divice_Info["model"]) # access the value of the key "model"

# Set
# Why need => this is needs for orginize data to retrive it easily.
# Set is a collection of unique items.
# Set is mutable and unordered.
# Set is used to store multiple items in a single variable.
# Set is used to store unique items.
# Set is used to perform mathematical set operations.
# set does not allow duplicate values.

device_Id = {1, 2, 3, 4, 5,5,5,5,8,9,7,1}
new_device_Id = {10, 11, 12, 13, 14}

print(len(device_Id)) # length of the set
print(device_Id.union(new_device_Id))# print the set
print(device_Id.intersection(new_device_Id)) # intersection of the set
print(device_Id.difference(new_device_Id)) # difference of the set


# Tuple
# Why need => this is needs for orginize data to retrive it easily.
# Tuple is a collection of ordered items.
# Tuple is immutable and ordered.
# Tuple is used to store multiple items in a single variable.
# Tuple is used to store duplicate items.
# Tuple is used to store heterogeneous items.

# Tuple is used to store items in a specific order.
# Tuple is used to store items in a specific order.

day_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(day_of_week[0]) # access the first item of the tuple
print(day_of_week[1]) # access the second item of the tuple
print(day_of_week[2]) # access the third item of the tuple
print(day_of_week[3]) # access the fourth item of the tuple

#Array
# Why need => this is needs for orginize data to retrive it easily.
# Array is a collection of ordered items.
# Array is mutable and ordered.
# Array is used to store multiple items in a single variable.
# Array is used to store duplicate items.
# Array is used to store heterogeneous items.

import array as arr
import random

# Create an array of integers
numbers = arr.array('i', [1, 2, 3, 4, 5])
print(numbers) # print the array

number = arr.array('i', [random.randint(1, 100) for i in range(5)]) # create an array of random numbers
print(number) # print the array
