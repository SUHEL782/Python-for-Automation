import boto3

s3 = boto3.resource('s3')

# Create the bucket (you may need to specify a region if not using us-east-1)
bucket_name = 'my-new-bucket'

# Optional: Specify region if needed
# s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})

s3.create_bucket(Bucket=bucket_name)

# Paths: no extra quotes and use raw string (r"...") or double backslashes
local_path = r"C:\Users\suhel\OneDrive\Desktop\Download from chrome\WhatsApp Image 2024-11-24 at 7.18.44 PM (1).jpeg"
object_key = "file.txt"

# Upload file
s3.Bucket(bucket_name).upload_file(local_path, object_key)

# Download file back (to a different location or same path)
s3.Bucket(bucket_name).download_file(object_key, local_path)

# Print available methods on the s3 object
print(dir(s3))
print("Bucket created and file uploaded successfully!")