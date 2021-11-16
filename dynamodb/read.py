#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# get a specific item from a table, specified by key
def get_item():
    table = dynamodb.Table('demo')
    try:
        response = table.get_item(
            Key={
                'item_key':'1a2b3c',
            }
        )
        item = response['Item']
        print(item)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_item()