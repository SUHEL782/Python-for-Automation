list1 = [1, 2, 3, 4, 5]
print(list1[1])
print(list1[0:3])
new_list = list1.append(6)
print(list1)
#update the value of the first element
list1[4] = 10
print(list1)
#delete the last elemen
list1.pop(4)
print(list1)

#apply all concept on aws devops practices
#create a new list
aws_services = ["EC2", "S3", "Lambda", "DynamoDB", "RDS"]
print(aws_services[2])  # Accessing an element
print(aws_services[1:4])  # Slicing the list
print(aws_services[-1])  # Accessing the last element


# use the tupple to store immutable data
aws_account_admin = ("admin","password123", "us-east-1", "arn:aws:iam::123456789012:user/admin")
print(aws_account_admin[0])  # Accessing the first element
