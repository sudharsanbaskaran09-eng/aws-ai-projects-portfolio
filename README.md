# AWS AI Projects Portfolio

A hands-on collection of 6 AI projects built on Amazon Web Services (AWS),
progressing from beginner to advanced level — built as part of my
Cloud AI Architect learning journey.

---

## About Me

- Fresher | Aspiring Cloud AI Architect
- Hands-on AWS AI/ML projects
- Python | boto3 | Serverless Architecture
- Chennai, India

---

## Projects

| # | Project | Services Used | Level |
|---|---------|--------------|-------|
| 1 | [Image Recognition App](./project-1-image-recognition) | S3, Rekognition, Lambda, API Gateway | Beginner |
| 2 | [Sentiment Analysis Dashboard](./project-2-sentiment-analysis) | Comprehend, Lambda, API Gateway, S3 | Beginner |
| 3 | [AI Document Scanner](./project-3-document-scanner) | Textract, S3, DynamoDB, Lambda | Intermediate |
| 4 | [Smart Chatbot](./project-4-smart-chatbot) | Lex, Lambda, DynamoDB | Intermediate |
| 5 | [GenAI App with Bedrock](./project-5-genai-bedrock) | Bedrock, Lambda, API Gateway | Advanced |
| 6 | [Document Q&A Bot RAG](./project-6-document-qa-rag) | Bedrock, S3, OpenSearch, Lambda | Advanced |

---

## Architecture Overview
```
User Request
     ↓
API Gateway        — REST API layer
     ↓
AWS Lambda         — Serverless compute
     ↓
AI Services        — Rekognition / Comprehend / Textract / Lex / Bedrock
     ↓
Storage            — S3 / DynamoDB / OpenSearch
```

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Cloud | Amazon Web Services (AWS) |
| Language | Python 3.x |
| SDK | boto3 |
| AI Services | Rekognition, Comprehend, Textract, Lex, Bedrock |
| Compute | AWS Lambda (Serverless) |
| Storage | Amazon S3, DynamoDB |
| API | Amazon API Gateway |
| Security | AWS IAM |

---

## Repo Structure
```
aws-ai-projects-portfolio/
├── README.md
├── project-1-image-recognition/
│     ├── README.md
│     ├── rekognition_app.py
│     ├── lambda_function.py
│     └── screenshots/
├── project-2-sentiment-analysis/
│     ├── README.md
│     ├── sentiment_app.py
│     ├── lambda_function.py
│     └── screenshots/
```

---

## How to Set Up

### Prerequisites
- AWS Account (Free Tier)
- Python 3.x installed
- AWS CLI installed and configured
- boto3 installed
```bash
pip install boto3
```

### Configure AWS CLI
```bash
aws configure
# Enter Access Key, Secret Key, Region: us-east-1, Output: json
```

---

## Certifications (In Progress)

- [ ] AWS Certified Cloud Practitioner
- [ ] AWS Certified Solutions Architect – Associate
- [ ] AWS Certified Machine Learning Specialty

---

## Screenshots

Every project has a dedicated screenshots folder with
step by step documentation of the entire build process.

---

## Connect

- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
