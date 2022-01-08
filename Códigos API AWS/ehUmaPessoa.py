import boto3
import base64
import requests
import json
import logging

def lambda_handler(event, context):
    try:
        body=json.loads(event['body'])
        file_name=body['file_name']
        bucket_name=body['bucket_name']
        client=boto3.client('rekognition')
        labels=client.detect_labels(
          Image={
              'S3Object': {
                  'Bucket': bucket_name,
                  'Name': file_name,
              }
          },
          MaxLabels=123,
          MinConfidence=77
        )
        return labels
    except Exception as e:
        print(e)
        raise(e)