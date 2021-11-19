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
# s3://cs4740-rekognition/tom-hanks.jpg

aws rekognition detect-faces \
    --image '{"S3Object":{"Bucket":"cs4740-rekognition","Name":"tom-hanks.jpg"}}' \
    --attributes "ALL"
