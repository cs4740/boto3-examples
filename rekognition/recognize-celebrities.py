#!/usr/bin/env python3

import boto3

# s3://cs4740-rekognition/tom-hanks.jpg

# aws rekognition recognize-celebrities \
#     --image '{"S3Object":{"Bucket":"cs4740-rekognition","Name":"tom-hanks.jpg"}}'

def recognize_celebrities(bucket, key):
    """
    Given an S3 bucket and key, return the celebrity names
    """
    client = boto3.client('rekognition')
    response = client.recognize_celebrities(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}})
    print(response)

recognize_celebrities('cs4740-rekognition', 'tom-hanks.jpg')