#loop
aws_services = ["EC2", "S3", "Lambda", "DynamoDB", "RDS"]
for service in aws_services:
        print(f"Service: {service}")  # Print each AWS service
        if service == "Lambda":
            print("Lambda is a serverless compute service.")
        else:
            print(f"{service} is a core AWS service.")