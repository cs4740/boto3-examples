#!/bin/bash

# uses aws-cli and jq to query dynamodb
aws dynamodb scan --table-name demo | jq -r .'Items'[].'favoriteFruit'.'S'