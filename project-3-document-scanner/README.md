# AI Document Scanner — AWS AI Project

## Overview
A serverless document scanning application built on AWS that automatically
extracts text from any document — images, invoices, receipts — using
Amazon Textract. Results are stored permanently in DynamoDB and accessible
via a REST API.

## Architecture
User → API Gateway → Lambda → Textract → DynamoDB → S3

## AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon Textract | AI-powered text extraction from documents |
| AWS Lambda | Serverless compute to process requests |
| Amazon API Gateway | REST API endpoint exposure |
| Amazon DynamoDB | Permanent storage of extracted results |
| Amazon S3 | Document upload and results storage |
| AWS IAM | Security, roles and permissions |

## Real World Use Cases
- Invoice and receipt processing automation
- Banking KYC document verification
- Insurance claim form extraction
- Healthcare patient record digitization

## Project Structure

```

project-3-document-scanner/
├── document_scanner.py      # Local script for document scanning
├── lambda_function.py       # Lambda handler for serverless execution
├── README.md
└── screenshots/

```

## Prerequisites
- AWS Account with Free Tier
- Python 3.x
- AWS CLI configured
- boto3 installed

## How to Run

### Local
```bash
pip install boto3
aws configure
python document_scanner.py
```

### API
```powershell
Invoke-WebRequest -Uri "https://your-api-url/prod/scan" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"bucket": "document-scanner-brat", "file_name": "your-document.jpg"}'
```

## Sample Output
```json
{
    "document_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "file_name": "sample_document.jpg",
    "total_lines": 50,
    "extracted_text": "Invoice Number: 12345\nDate: 2024-01-15\nTotal: $250.00",
    "message": "Document scanned successfully!"
}
```

## Author
Sudharsan
- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
