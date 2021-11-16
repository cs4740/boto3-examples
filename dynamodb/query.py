#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key, Attr
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# search the table by the primary key. Can use operators like .eq, .lt, .gt, etc.
def query_items():
    table = dynamodb.Table('demo')
    try:
        response = table.query(
            KeyConditionExpression=Key('item_key').eq('1a2b3c')
        )
        items = response['Items']
        print(items)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    query_items()