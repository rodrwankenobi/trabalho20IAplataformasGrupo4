import json
import boto3
import uuid
import base64

def lambda_handler(event, context):
    content = base64.b64decode(event['body'])
    filename=f'analise_credito_{uuid.uuid1()}.jpg'
    s3 = boto3.client('s3')
    s3.put_object(Body=content,Bucket='trabalho-plataformas-20ia-grupo4',Key=filename)
    return filename