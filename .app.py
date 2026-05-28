import boto3

# Create S3 client
s3 = boto3.client('ec2')

# List all S3 buckets
response = s3.list_buckets()

print("S3 Buckets:")

for bucket in response['Buckets']:
    print(bucket['production'])
