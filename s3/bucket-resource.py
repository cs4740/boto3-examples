import boto3

# High level wrapper of client - limited methods
s3 = boto3.resource("s3")
bucket = s3.Bucket("cs4740-resources")

# fetches name of bucket only
print(bucket)

# Show all class methods
print(dir(bucket))
