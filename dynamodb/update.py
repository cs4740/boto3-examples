#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# update a single record in a table
def update_item():
    table = dynamodb.Table('demo')
    try:
        response = table.update_item(
            Key={
                'item_key':'1a2b3c'
            },
            UpdateExpression='SET favoriteFruit = :fruit',
            ExpressionAttributeValues={
                ':fruit': 'blueberry'
            },
        )
        print(response)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    update_item()