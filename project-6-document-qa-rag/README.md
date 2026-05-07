# Document Q&A Bot (RAG Architecture) — AWS AI Project

## Overview
A serverless Retrieval Augmented Generation (RAG) application built on AWS
that answers questions based on a custom knowledge base stored in S3.
Uses Amazon Nova Lite via Bedrock for answer generation and retrieves
context from documents before generating responses — ensuring accurate,
grounded AI answers.

## Architecture
User → API Gateway → Lambda → S3 (retrieve context) → Bedrock Nova Lite → Answer

## How RAG Works
1. User sends a question via API
2. System loads knowledge base from S3
3. Finds most relevant document sections for the question
4. Sends question + relevant context to Bedrock
5. Bedrock generates accurate answer based only on the context
6. Answer returned to user via API

## AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon Bedrock | GenAI foundation model inference |
| Amazon Nova Lite | Text generation — fast and cost efficient |
| Amazon S3 | Knowledge base document storage |
| AWS Lambda | Serverless RAG pipeline execution |
| Amazon API Gateway | REST API endpoint exposure |
| AWS IAM | Security, roles and permissions |

## Real World Use Cases
- Enterprise document Q&A systems
- Customer support knowledge base bots
- Legal and compliance document assistants
- HR policy and onboarding assistants

## Project Structure
```
project-6-document-qa-rag/
├── rag_app.py               # Local RAG pipeline script
├── lambda_function.py       # Lambda handler for serverless RAG
├── knowledge_base.txt       # Sample knowledge base document
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
python rag_app.py
```
### API
```Powershell
Invoke-WebRequest -Uri "https://your-api-url/prod/ask" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"question": "What is Amazon Bedrock?"}'
```
### Sample Output
```json
{
    "question": "What is Amazon Bedrock?",
    "answer": "Amazon Bedrock is a fully managed service that provides
    access to foundation models from leading AI companies through a
    single API. It enables developers to build GenAI applications
    without managing any ML infrastructure.",
    "chunks_used": 3,
    "model": "amazon.nova-lite-v1:0"
}
```
### Author
Sudharsan Baskaran

LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a

GitHub: https://github.com/sudharsanbaskaran09-eng

