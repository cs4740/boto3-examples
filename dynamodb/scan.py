#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key, Attr
import botocore.exceptions

dynamodb = boto3.resource('dynamodb')

# scan a table by an arbirtary column value. Uses operators like .eq, .lt, .gt, etc.
def scan_items():
    table = dynamodb.Table('demo')
    try:
        response = table.scan(
            FilterExpression=Attr('favoriteNumber').lt(24)
        )
        items = response['Items']
        print(items)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    scan_items()