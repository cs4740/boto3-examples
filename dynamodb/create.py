#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# add one item to the table. must have unique key.
def insert_item():
    table = dynamodb.Table('demo')
    try:
        response = table.put_item(
            Item={
                'item_key':'3d4e5f',
                'favoriteFruit':'Blueberry',
                'favoriteNumber':23,
                'favoriteColor':'Yellow',
                'person':'Ming'
            }
        )
        print(response)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    insert_item()