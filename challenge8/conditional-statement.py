instance_type = input("Enter your instance type (e.g., t2.micro): ")

if instance_type == "t2.micro":
    print("Thanks for using t2.micro")
else:
    print("You are not eligible for t2.medium because you are using the free tier")
