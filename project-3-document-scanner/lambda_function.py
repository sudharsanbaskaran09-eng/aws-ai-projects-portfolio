import boto3
import json
import uuid
from datetime import datetime

textract_client = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = 'DocumentResults'

def lambda_handler(event, context):

    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event

    bucket_name = body['bucket']
    file_name = body['file_name']

    # Extract text with Textract
    response = textract_client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': f'documents/{file_name}'
            }
        }
    )

    # Get all text lines
    extracted_lines = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_lines.append(block['Text'])

    full_text = '\n'.join(extracted_lines)

    # Save to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    document_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'document_id': document_id,
            'file_name': file_name,
            'extracted_text': full_text,
            'total_lines': len(extracted_lines),
            'timestamp': datetime.now().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'document_id': document_id,
            'file_name': file_name,
            'total_lines': len(extracted_lines),
            'extracted_text': full_text,
            'message': 'Document scanned successfully!'
        })
    }
