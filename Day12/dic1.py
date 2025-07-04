# dictionary
aws_services = {
    "ec2": "Elastic Compute Cloud",
    "s3": "Simple Storage Service",
    "lambda": "Serverless Compute Service",
    "dynamodb": "NoSQL Database Service",
}
aws_instances = {
    "t2.micro": "General Purpose",
    "t2.small": "General Purpose",
    "t2.medium": "General Purpose",
    "m5.large": "Compute Optimized",
}

print("aws_instances:", aws_instances["t2.small"])  # Accessing a value using a key
for aws_instance, description in aws_instances.items():
    print(f"Instance Type: {aws_instance}, Description: {description}")  # Print each AWS instance type and its description
# Adding a new key-value pair to the dictionary
# aws_instances["m5.xlarge"] = "Compute Optimized"
# print("Updated aws_instances:", aws_instances)
# replace 
aws_instances["t2.micro"] = "General Purpose - Updated"
print("Replaced aws_instances:", aws_instances)

# Deleting a key-value pair from the dictionary
del aws_instances["t2.small"]
print("After deletion aws_instances:", aws_instances)
