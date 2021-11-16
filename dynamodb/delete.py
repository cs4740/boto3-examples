#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# delete an item from a table, specified by key
def delete_item():
    table = dynamodb.Table('demo')
    try:
        response = table.delete_item(
            Key={
                'item_key':'1a2b3c',
            }
        )
        print(response)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    delete_item()