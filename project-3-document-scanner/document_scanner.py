import boto3
import json
import uuid
from datetime import datetime

# Initialize AWS clients
s3_client = boto3.client('s3', region_name='us-east-1')
textract_client = boto3.client('textract', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

BUCKET_NAME = 'document-scanner-brat'
TABLE_NAME = 'DocumentResults'

def upload_document(file_path, file_name):
    """Upload document to S3"""
    print(f"\n📤 Uploading {file_name} to S3...")
    s3_client.upload_file(file_path, BUCKET_NAME, f'documents/{file_name}')
    print(f"✅ Upload successful!")

def extract_text_from_document(file_name):
    """Send document to Textract for text extraction"""
    print(f"\n🤖 Extracting text with Amazon Textract...")

    response = textract_client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': BUCKET_NAME,
                'Name': f'documents/{file_name}'
            }
        }
    )

    # Extract all text blocks
    extracted_text = []
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text.append(block['Text'])

    full_text = '\n'.join(extracted_text)

    print("\n📄 Extracted Text:")
    print("=" * 50)
    print(full_text)
    print("=" * 50)
    print(f"\n✅ Total lines extracted: {len(extracted_text)}")

    return full_text, extracted_text

def save_to_dynamodb(file_name, full_text, lines):
    """Save extracted text to DynamoDB"""
    print(f"\n💾 Saving results to DynamoDB...")

    table = dynamodb.Table(TABLE_NAME)

    document_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    table.put_item(
        Item={
            'document_id': document_id,
            'file_name': file_name,
            'extracted_text': full_text,
            'total_lines': len(lines),
            'timestamp': timestamp
        }
    )

    print(f"✅ Saved to DynamoDB!")
    print(f"   Document ID : {document_id}")
    print(f"   File Name   : {file_name}")
    print(f"   Total Lines : {len(lines)}")
    print(f"   Timestamp   : {timestamp}")

    return document_id

def save_results_to_s3(file_name, full_text, document_id):
    """Save results as JSON to S3"""
    result = {
        'document_id': document_id,
        'file_name': file_name,
        'extracted_text': full_text,
        'timestamp': datetime.now().isoformat()
    }

    result_file = file_name.replace('.', '_') + '_results.json'
    with open(result_file, 'w') as f:
        json.dump(result, f, indent=4)

    s3_client.upload_file(result_file, BUCKET_NAME, f'results/{result_file}')
    print(f"\n☁️ Results saved to S3: results/{result_file}")

# ---- MAIN ----
if __name__ == "__main__":
    FILE_PATH = "sample_document.jpg"
    FILE_NAME = "sample_document.jpg"

    upload_document(FILE_PATH, FILE_NAME)
    full_text, lines = extract_text_from_document(FILE_NAME)
    document_id = save_to_dynamodb(FILE_NAME, full_text, lines)
    save_results_to_s3(FILE_NAME, full_text, document_id)

    print("\n🎉 Document scanning complete!")
