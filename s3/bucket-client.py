import boto3

# Low level: all methods
s3 = boto3.client("s3")

all_buckets = s3.list_buckets()
# print(all_buckets)

list_bucket = s3.list_objects(
    Bucket='cs4740-resources'
  )
print(list_bucket)
