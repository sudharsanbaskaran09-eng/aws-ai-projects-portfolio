# AWS AI Projects Portfolio

A practical portfolio of six serverless AI and generative AI projects built with AWS managed services. The projects progress from computer vision and natural-language processing to document intelligence, conversational applications, foundation models, and retrieval-augmented generation (RAG).

The examples are designed for learning and portfolio demonstration. Each project includes a local Python entry point, AWS service integration, sample outputs or screenshots where available, and a project-specific README when documentation is available.

## Projects at a Glance

| # | Project | What it demonstrates | Primary AWS services |
|---|---|---|---|
| 1 | [Image Recognition](./project-1-image-recognition/) | Detects objects, scenes, and labels in images and returns confidence scores | Amazon Rekognition, AWS Lambda, Amazon S3, Amazon API Gateway |
| 2 | [Sentiment Analysis](./project-2-sentiment-analysis/) | Classifies text as positive, negative, neutral, or mixed with confidence scores | Amazon Comprehend, AWS Lambda, Amazon S3, Amazon API Gateway |
| 3 | [AI Document Scanner](./project-3-document-scanner/) | Extracts text from images and documents, then persists the results | Amazon Textract, AWS Lambda, Amazon S3, Amazon DynamoDB, Amazon API Gateway |
| 4 | [Smart Chatbot](./project-4-smart-chatbot/) | Provides keyword-based chatbot responses and stores conversation history by session | AWS Lambda, Amazon DynamoDB, Amazon API Gateway |
| 5 | [Generative AI with Bedrock](./project-5-genai-bedrock/) | Generates text from prompts using Amazon Nova Micro through the Bedrock Converse API | Amazon Bedrock, Amazon Nova Micro, AWS Lambda, Amazon API Gateway |
| 6 | [Document Q&A with RAG](./project-6-document-qa-rag/) | Retrieves relevant knowledge-base sections and uses Amazon Nova Lite to generate grounded answers | Amazon Bedrock, Amazon Nova Lite, Amazon S3, AWS Lambda, Amazon API Gateway |

## Architecture Overview

Most projects follow a serverless request flow:

```text
User or client
    → Amazon API Gateway
    → AWS Lambda
    → AWS AI service
    → Amazon S3 or Amazon DynamoDB
    → JSON response
```

The RAG project uses a retrieval-and-generation flow:

```text
Question → API Gateway → Lambda → S3 knowledge base
         → keyword retrieval → Amazon Nova Lite → grounded answer
```

## Project Details

### 1. Image Recognition

The image recognition application uploads or references an image in Amazon S3 and uses Amazon Rekognition to detect labels such as people, objects, scenes, and outdoor environments. Results include confidence scores and can be returned through a REST API.

**Typical use cases:**

- Product image tagging for e-commerce
- Security and surveillance analysis
- Social media content moderation
- Image classification workflows

[Read the project documentation →](./project-1-image-recognition/README.md)

### 2. Sentiment Analysis

The sentiment analysis application sends text to Amazon Comprehend and returns a sentiment classification—`POSITIVE`, `NEGATIVE`, `NEUTRAL`, or `MIXED`—along with confidence scores. It provides a foundation for analyzing reviews, feedback, and support content.

**Typical use cases:**

- Customer review analysis
- Brand and social media monitoring
- Support-ticket prioritization
- Product feedback classification

[Read the project documentation →](./project-2-sentiment-analysis/README.md)

### 3. AI Document Scanner

The document scanner stores a document in Amazon S3, uses Amazon Textract to extract text line by line, and persists the extracted content and metadata in Amazon DynamoDB. A JSON result can also be written back to S3.

**Typical use cases:**

- Invoice and receipt processing
- Banking and KYC document verification
- Insurance claim extraction
- Healthcare record digitization

[Read the project documentation →](./project-3-document-scanner/README.md)

### 4. Smart Chatbot

The smart chatbot exposes a REST endpoint backed by AWS Lambda. It matches user messages against common intents such as greetings, AWS services, contact information, and help requests. Each interaction is stored in the `ChatHistory` DynamoDB table using a session ID, providing a simple foundation for conversation history.

**Typical use cases:**

- Website customer support
- FAQ bots for web and mobile applications
- HR onboarding assistants
- E-commerce product inquiry bots

[Read the project documentation →](./project-4-smart-chatbot/README.md)

### 5. Generative AI with Amazon Bedrock

This project demonstrates prompt-based text generation with Amazon Bedrock. The local application sends several prompts to the Amazon Nova Micro foundation model and saves each response as JSON. The Lambda handler exposes the same capability as an API and accepts a `prompt` field in the request body.

Example prompts include explanations of AWS, serverless computing, and an AWS Cloud AI Architect job description.

[Open the project →](./project-5-genai-bedrock/)

### 6. Document Q&A with RAG

The RAG application loads a knowledge base from S3, splits it into paragraphs, ranks sections using keyword overlap with the question, and sends the selected context to Amazon Nova Lite. The prompt instructs the model to answer only from the retrieved context and to acknowledge when the information is unavailable.

**Typical use cases:**

- Enterprise document question answering
- Customer-support knowledge bases
- Legal and compliance assistants
- HR policy and onboarding assistants

[Read the project documentation →](./project-6-document-qa-rag/README.md)

## Repository Structure

```text
aws-ai-projects-portfolio/
├── project-1-image-recognition/
│   ├── rekognition_app.py
│   ├── lambda_function.py
│   ├── results.json
│   ├── screenshots/
│   └── README.md
├── project-2-sentiment-analysis/
│   ├── sentiment_app.py
│   ├── lambda_function.py
│   ├── screenshots/
│   └── README.md
├── project-3-document-scanner/
│   ├── document_scanner.py
│   ├── lambda_function.py
│   ├── screenshots/
│   └── README.md
├── project-4-smart-chatbot/
│   ├── chatbot_client.py
│   ├── lambda_function.py
│   ├── screenshots/
│   └── README.md
├── project-5-genai-bedrock/
│   ├── bedrock_app.py
│   ├── lambda_function.py
│   ├── response1.json
│   ├── response2.json
│   ├── response3.json
│   └── SCREENSHOTS/
├── project-6-document-qa-rag/
│   ├── rag_app.py
│   ├── lambdacode.py
│   ├── knowledge_base.txt
│   ├── screenshots/
│   └── README.md
└── README.md
```

## AWS Services Used

- **Amazon Rekognition** — Image analysis and label detection
- **Amazon Comprehend** — Natural-language processing and sentiment analysis
- **Amazon Textract** — Text extraction from scanned documents and images
- **Amazon Bedrock** — Foundation-model access for generative AI applications
- **Amazon Nova Micro** — Fast, cost-conscious text generation for Project 5
- **Amazon Nova Lite** — Text generation for grounded answers in Project 6
- **AWS Lambda** — Serverless application and API logic
- **Amazon API Gateway** — REST API exposure
- **Amazon S3** — Image, document, result, and knowledge-base storage
- **Amazon DynamoDB** — Chat history and document-result persistence
- **AWS IAM** — Roles, permissions, and access control

## Prerequisites

- An AWS account with access to the services used by the selected project
- Python 3.x
- AWS CLI installed and configured
- `boto3` installed for AWS SDK examples
- `requests` installed for the chatbot client
- Bedrock model access enabled in the selected AWS Region for Projects 5 and 6
- IAM permissions for the relevant S3, Lambda, DynamoDB, Rekognition, Comprehend, Textract, and Bedrock operations

## Getting Started

```bash
git clone https://github.com/sudharsanbaskaran09-eng/aws-ai-projects-portfolio.git
cd aws-ai-projects-portfolio
pip install boto3 requests
aws configure
```

Choose a project and follow its README for project-specific resources, bucket names, tables, API paths, and deployment steps:

- [Project 1: Image Recognition](./project-1-image-recognition/README.md)
- [Project 2: Sentiment Analysis](./project-2-sentiment-analysis/README.md)
- [Project 3: Document Scanner](./project-3-document-scanner/README.md)
- [Project 4: Smart Chatbot](./project-4-smart-chatbot/README.md)
- [Project 5: Generative AI with Bedrock](./project-5-genai-bedrock/)
- [Project 6: Document Q&A with RAG](./project-6-document-qa-rag/README.md)

## Example API Payloads

The exact API URL depends on your API Gateway deployment. The examples below show the request shapes expected by the Lambda handlers.

```json
// Image recognition
{"bucket": "your-bucket", "image": "your-image.jpg"}

// Sentiment analysis
{"text": "The service was excellent."}

// Document scanner
{"bucket": "document-scanner-brat", "file_name": "your-document.jpg"}

// Smart chatbot
{"message": "What services do you provide?", "session_id": "user-001"}

// Generative AI
{"prompt": "Explain serverless computing in three sentences."}

// Document Q&A
{"question": "What is Amazon Bedrock?"}
```

## Security and Cost Notes

- Apply least-privilege IAM policies to Lambda and local development identities.
- Never commit AWS access keys, secrets, or production data.
- Review S3 bucket policies and block unintended public access.
- Enable encryption and consider versioning for important S3 data.
- Validate and sanitize API input before sending it to downstream services.
- Configure CORS narrowly for production applications instead of using `*`.
- Monitor CloudWatch logs, AWS Budgets, and service usage while experimenting.
- Bedrock, Textract, Comprehend, Rekognition, S3, DynamoDB, and API Gateway usage may incur charges.
- Delete test resources and stored data when experimentation is complete.

## Learning Path

A useful progression through the portfolio is:

1. Start with **Image Recognition** and **Sentiment Analysis** to learn managed AI APIs.
2. Continue with the **Document Scanner** to combine AI processing with persistent storage.
3. Explore the **Smart Chatbot** to understand API-driven conversational workflows.
4. Move to **Generative AI with Bedrock** for foundation-model inference.
5. Finish with **Document Q&A with RAG** to learn how retrieval can ground model responses in application data.

## Author

**Sudharsan Baskaran**

- LinkedIn: [sudharsan-baskaran-95443925a](https://linkedin.com/in/sudharsan-baskaran-95443925a)
- GitHub: [sudharsanbaskaran09-eng](https://github.com/sudharsanbaskaran09-eng)

## License

This repository is intended for learning and portfolio demonstration. Add an open-source license file before distributing or reusing the code publicly.




