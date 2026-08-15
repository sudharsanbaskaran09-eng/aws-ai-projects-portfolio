# AWS AI Projects Portfolio

A compact portfolio of six serverless AWS AI demo projects that showcase practical uses of AWS AI/ML services (Rekognition, Comprehend, Textract, Bedrock/Titan, DynamoDB, S3). Each project is a small, runnable example exposing a Lambda-based REST API and local scripts so engineers can explore cloud-native AI integrations and patterns.

## Projects

- project-1-image-recognition — Image analysis demo using Amazon Rekognition
- project-2-sentiment-analysis — Sentiment analysis demo using Amazon Comprehend
- project-3-document-scanner — Document OCR & extra
- project-4-smart-chatbot — Chatbot demo storing chats in DynamoDB
- project-5-genai-bedrock — Generative AI demo using Amazon Bedrock (Titan)
- project-6-document-qa-rag — RAG-based Q&A demo (S3 + Bedrock / Nova Lite)

Each project contains a small set of Python scripts, a Lambda handler (for serverless deployment), example outputs, and screenshots demonstrating results.

## Stack

- **Language:** Python 3.x
- **Runtime / Pattern:** AWS Lambda + API Gateway (serverless)
- **Notable libraries / services:** boto3, requests, Amazon Rekognition, Amazon Comprehend, Amazon Textract, Amazon Bedrock (Titan / Nova), Amazon S3, Amazon DynamoDB

## How it's organized

```
project-1-image-recognition/       # Image analysis (Rekognition)
project-2-sentiment-analysis/      # Text sentiment (Comprehend)
project-3-document-scanner/        # Document OCR (Textract)
project-4-smart-chatbot/           # Chatbot (DynamoDB storage)
project-5-genai-bedrock/           # GenAI (Bedrock / Titan)
project-6-document-qa-rag/         # RAG Q&A (S3 + Bedrock Nova Lite)
```

How it fits together:
- Each project follows the pattern: User → API Gateway → Lambda → (AI service) → Storage (S3 / DynamoDB) → Response.
- Local scripts (e.g., `bedrock_app.py`, `rag_app.py`, `document_scanner.py`) let you run and test functionality outside Lambda; Lambda handlers provide the same pipeline when deployed.

## Quickstart (run a project locally)

1. Clone the repo:

```bash
git clone https://github.com/sudharsanbaskaran09-eng/aws-ai-projects-portfolio.git
cd aws-ai-projects-portfolio
```

2. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install boto3 requests
```

3. Configure AWS credentials (required for service calls):

```bash
aws configure
```

4. Run a local test script (example: document scanner):

```bash
cd project-3-document-scanner
python document_scanner.py
```

5. To call a deployed API, use curl or PowerShell and replace the example URL with your API Gateway URL:

```bash
curl -X POST "https://your-api-url/prod/scan" -H "Content-Type: application/json" \
  -d '{"bucket":"your-bucket","file_name":"sample.jpg"}'
```

## Deployment notes

- Deploy each project as a Lambda function behind API Gateway. Ensure the Lambda execution role has permissions for the required services (Rekognition, Comprehend, Textract, Bedrock, S3, DynamoDB).
- Bedrock-based projects (project-5 and project-6) require Bedrock account access and model permissions; enable Bedrock in your AWS account before using those demos.
- Create the necessary S3 buckets and DynamoDB tables referenced by the project scripts.

## Try asking
- "Which project stores chat history in DynamoDB and where is the local client?" — project-4-smart-chatbot (see `chatbot_client.py`)
- "How do I run the RAG demo locally and which file contains the sample knowledge base?" — project-6-document-qa-rag (`rag_app.py`, `knowledge_base.txt`)
- "Which projects use Bedrock and what steps are needed to enable model access?" — project-5-genai-bedrock and project-6-document-qa-rag; Bedrock access must be enabled in your AWS account.

## Author
Sudharsan Baskaran — https://github.com/sudharsanbaskaran09-eng | https://linkedin.com/in/sudharsan-baskaran-95443925a













