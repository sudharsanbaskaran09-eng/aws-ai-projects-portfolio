# Image Recognition App — AWS AI Project

## Overview
A serverless image recognition application built on AWS that automatically
detects objects, scenes, and labels in images using Amazon Rekognition.
Designed to demonstrate real-world AI integration with cloud-native architecture.

## Architecture
User → API Gateway → Lambda → Rekognition → S3

## AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon Rekognition | AI-powered image analysis and label detection |
| AWS Lambda | Serverless compute to process requests |
| Amazon API Gateway | REST API endpoint exposure |
| Amazon S3 | Image upload and results storage |
| AWS IAM | Security, roles and permissions |

## Real World Use Cases
- Automatic product image tagging for e-commerce platforms
- Security and surveillance content analysis
- Social media content moderation pipelines
- Medical imaging classification systems

## Project Structure
```
project-1-image-recognition/
├── rekognition_app.py       # Local script to upload and analyze images
├── lambda_function.py       # Lambda handler for serverless execution
├── results.json             # Sample AI output
└── screenshots/             # Step by step project documentation
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
python rekognition_app.py
```

### API
```bash
Invoke-WebRequest -Uri "https://your-api-url/prod/analyze" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"bucket": "your-bucket", "image": "your-image.jpg"}'
```

## Sample Output
```json
[
    { "Name": "Person", "Confidence": 99.81 },
    { "Name": "Outdoors", "Confidence": 97.45 },
    { "Name": "Nature", "Confidence": 95.12 }
]
```

## Author
Sudharsan 
- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
