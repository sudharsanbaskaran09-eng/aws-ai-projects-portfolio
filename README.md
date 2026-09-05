# AWS AI Projects Portfolio

A collection of six serverless AI demo projects that showcase AWS services applied to real-world tasks: image recognition, sentiment analysis, document scanning, a smart chatbot, GenAI with Bedrock, and a document Q&A (RAG) system. Each project is a small, self-contained Python app with Lambda handlers and sample outputs to illustrate how to integrate AWS AI services in a cloud-native way.

## Highlights
- 6 example projects demonstrating AWS AI services and serverless architecture
- Implementations in Python using AWS SDK (boto3)
- Lambda handlers and local scripts for quick experimentation
- Sample outputs and screenshots included per project

## Projects
- project-1-image-recognition — Image analysis using Amazon Rekognition (rekognition_app.py, results.json)
- project-2-sentiment-analysis — Text sentiment classification using Amazon Comprehend (sentiment_app.py, lambda_function.py)
- project-3-document-scanner — Document OCR/extraction using Amazon Textract (document_scanner.py, lambda_function.py)
- project-4-smart-chatbot — Chatbot example (chatbot_client.py, lambda_function.py)
- project-5-genai-bedrock — GenAI demos with Bedrock (bedrock_app.py, lambda_function.py, response*.json)
- project-6-document-qa-rag — Document question-answering with a RAG-style flow (rag_app.py, lambdacode.py, knowledge_base.txt)

## Stack
- **Language(s):** Python 3.x
- **Runtime / Pattern:** Serverless (AWS Lambda) + local Python scripts for testing
- **Notable libraries / services:** boto3, Amazon Rekognition, Amazon Comprehend, Amazon Textract, Amazon DynamoDB, Amazon S3, Amazon Bedrock (GenAI)

## Repository layout
```
project-1-image-recognition/    # Rekognition demo (rekognition_app.py, results.json, screenshots/)
project-2-sentiment-analysis/   # Comprehend demo (sentiment_app.py, lambda_function.py, screenshots/)
project-3-document-scanner/     # Textract demo (document_scanner.py, lambda_function.py, screenshots/)
project-4-smart-chatbot/        # Chatbot demo (chatbot_client.py, lambda_function.py, screenshots/)
project-5-genai-bedrock/        # Bedrock GenAI demo (bedrock_app.py, lambda_function.py, response*.json, SCREENSHOTS/)
project-6-document-qa-rag/      # Document QA / RAG demo (rag_app.py, lambdacode.py, knowledge_base.txt, screenshots/)
README.md                       # This file
```

## How it fits together
Each project contains:
- A local helper script (e.g., rekognition_app.py, sentiment_app.py) you can run to test the feature locally.
- A Lambda handler (lambda_function.py) that contains the serverless entry point intended to be triggered via API Gateway or other AWS events.
- Sample outputs and screenshots demonstrating expected responses.

## Quickstart — common prerequisites
1. Install Python 3.x
2. Install boto3:
   ```bash
   pip install boto3
   ```
3. Configure AWS CLI with credentials that have permissions to the required services:
   ```bash
   aws configure
   ```
4. Ensure the IAM role or user has the proper permissions for the services used by the project you want to run (S3, Lambda, Rekognition, Comprehend, Textract, DynamoDB, Bedrock, etc.)

## Run a project locally
- Image Recognition (project-1-image-recognition)
  ```bash
  cd project-1-image-recognition
  pip install boto3
  aws configure
  python rekognition_app.py
  ```

- Sentiment Analysis (project-2-sentiment-analysis)
  ```bash
  cd project-2-sentiment-analysis
  pip install boto3
  aws configure
  python sentiment_app.py
  ```

- Document Scanner (project-3-document-scanner)
  ```bash
  cd project-3-document-scanner
  pip install boto3
  aws configure
  python document_scanner.py
  ```

- Smart Chatbot (project-4-smart-chatbot)
  ```bash
  cd project-4-smart-chatbot
  pip install boto3
  aws configure
  python chatbot_client.py
  ```

- GenAI Bedrock (project-5-genai-bedrock)
  ```bash
  cd project-5-genai-bedrock
  pip install boto3
  aws configure
  python bedrock_app.py
  ```

- Document QA / RAG (project-6-document-qa-rag)
  ```bash
  cd project-6-document-qa-rag
  pip install boto3
  aws configure
  python rag_app.py
  ```

(Replace these python commands with your own invocation patterns if the script accepts CLI arguments or requires specific input files. Many projects include sample JSON or screenshot directories with examples.)

## Deploying as Lambda (general guidance)
- Package project files and dependencies (or use a Lambda layer).
- Create an IAM role with the minimum required permissions for the AWS services the project uses.
- Create a Lambda function using the provided lambda_function.py as the handler.
- (Optional) Create an API Gateway endpoint and integrate it with the Lambda function for HTTP access.
- Test with the included sample payloads / sample outputs.

## Security & IAM
- These projects interact with AWS services — follow the principle of least privilege when creating IAM roles.
- Do not embed long-lived credentials in code. Use IAM roles for Lambda or environment variables managed via AWS Secrets Manager / Parameter Store when necessary.

## Examples of sample output
- Image recognition sample:
  ```json
  [
    { "Name": "Person", "Confidence": 99.81 },
    { "Name": "Outdoors", "Confidence": 97.45 }
  ]
  ```

- Sentiment analysis sample:
  ```json
  {
    "sentiment": "POSITIVE",
    "scores": { "Positive": 0.9997, "Negative": 0.0001, "Neutral": 0.0001, "Mixed": 0.0001 }
  }
  ```

## Notes & next steps
- Add an explicit LICENSE file if you want to open-source these projects under a specific license.
- Add CI/CD or AWS SAM / CloudFormation / CDK templates to streamline deployment and reproducible infrastructure.
- If you want to turn a demo into a reusable module, extract shared AWS setup and common utilities into a common folder.

## Contributing
- Contributions, bug reports, and improvements are welcome. Open issues or pull requests with a clear description of the change and motivation.

## Author
- Sudharsan Baskaran
  - LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
  - GitHub: https://github.com/sudharsanbaskaran09-eng

