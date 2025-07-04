#for loop - you know how many times excute the block of code you can used for loop
aws_services = ["EC2", "S3", "Lambda", "DynamoDB", "RDS"]
for service in aws_services:
        print(f"Service: {service}")  # Print each AWS service
        if service == "Lambda":
            print("Lambda is a serverless compute service.")
        else:
            print(f"{service} is a core AWS service.")


            # while loop - you don't know how many times excute the block of code you can used while loop

aws_services1 = ["EC2", "S3", "Lambda", "DynamoDB", "RDS"]
index = 0
while index < len(aws_services1):
    service = aws_services1[index]
    print(f"Service: {service}")  # Print each AWS service
    if service == "Lambda":
        print("Lambda is a serverless compute service.")
    else:
        print(f"{service} is a core AWS service.")
    index += 1  # Increment the index to avoid infinite loop

