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
