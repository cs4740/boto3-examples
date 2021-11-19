#!/bin/bash

set -e

# --image format in JSON:
# {
#   "Bytes": blob,
#   "S3Object": {
#     "Bucket": "string",
#     "Name": "string",
#     "Version": "string"
#   }
# }
# s3://cs4740-rekognition/coffee-maker.png

aws rekognition detect-labels --image '{"S3Object":{"Bucket":"cs4740-rekognition","Name":"coffee-maker.png"}}'