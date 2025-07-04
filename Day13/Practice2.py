aws_instance = {
    "instance_type": "t2.micro",
    "ami": "ami-12345678",
    "region": "us-west-2",
    "availability_zone": "us-west-2a",
    "security_groups": ["sg-12345678", "sg-87654321"]
}
# Accessing values in the dictionary
print("Instance Type:", aws_instance["instance_type"])

print("Region: ", aws_instance["region"])

security_groups = aws_instance["security_groups"]
print("Security Groups:", security_groups)
aws_instance["instance_name"] = "my_first_instance"
print("Updated Instance Name:", aws_instance["instance_name"])
