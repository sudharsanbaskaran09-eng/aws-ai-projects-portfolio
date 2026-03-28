# Sentiment Analysis Dashboard — AWS AI Project

## Overview
A serverless sentiment analysis application built on AWS that classifies
text as Positive, Negative, Neutral, or Mixed using Amazon Comprehend.
Built to demonstrate real-world NLP integration with cloud-native serverless
architecture on AWS.

## Architecture
User → API Gateway → Lambda → Comprehend → S3

## AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon Comprehend | AI-powered NLP and sentiment detection |
| AWS Lambda | Serverless compute to process requests |
| Amazon API Gateway | REST API endpoint exposure |
| Amazon S3 | Input text and results storage |
| AWS IAM | Security, roles and permissions |

## Real World Use Cases
- Customer review analysis for e-commerce platforms
- Social media monitoring and brand sentiment tracking
- Support ticket prioritization based on urgency
- Product feedback classification pipelines

## Project Structure
```
project-2-sentiment-analysis/
├── sentiment_app.py         # Local script for batch sentiment analysis
├── lambda_function.py       # Lambda handler for serverless execution
├── sentiment_results.json   # Sample AI output
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
python sentiment_app.py
```

### API
```bash
Invoke-WebRequest -Uri "https://your-api-url/prod/sentiment" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"text": "Your text here"}'
```

## Sample Output
```json
{
    "sentiment": "POSITIVE",
    "scores": {
        "Positive": 0.9997,
        "Negative": 0.0001,
        "Neutral": 0.0001,
        "Mixed": 0.0001
    },
    "message": "Text sentiment is POSITIVE"
}
```

## Author
Sudharsan 
- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
