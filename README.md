# AWS AI Projects Portfolio

A collection of serverless artificial intelligence projects built with AWS managed services. This portfolio demonstrates how cloud-native applications can integrate computer vision and natural language processing capabilities into practical, scalable workflows.

## Projects

| Project | Description | AWS AI Service |
|---|---|---|
| [Image Recognition](./project-1-image-recognition/) | Detects objects, scenes, and labels in images | Amazon Rekognition |
| [Sentiment Analysis Dashboard](./project-2-sentiment-analysis/) | Classifies text as positive, negative, neutral, or mixed | Amazon Comprehend |

## Architecture Pattern

Both projects use a serverless architecture that minimizes infrastructure management and scales automatically:

```text
User → Amazon API Gateway → AWS Lambda → AWS AI Service → Amazon S3
```

## AWS Services Used

- **Amazon Rekognition** — Image analysis and label detection
- **Amazon Comprehend** — Natural language processing and sentiment analysis
- **AWS Lambda** — Serverless application logic
- **Amazon API Gateway** — REST API exposure
- **Amazon S3** — Input and output storage
- **AWS IAM** — Access control and permissions management

## Repository Structure

```text
aws-ai-projects-portfolio/
├── project-1-image-recognition/
│   ├── lambda_function.py
│   ├── rekognition_app.py
│   ├── results.json
│   ├── screenshots/
│   └── README.md
├── project-2-sentiment-analysis/
│   ├── lambda_function.py
│   ├── sentiment_app.py
│   ├── sentiment_results.json
│   ├── screenshots/
│   └── README.md
└── README.md
```

## Prerequisites

- An AWS account
- Python 3.x
- AWS CLI installed and configured
- Appropriate IAM permissions for the AWS services used
- `boto3` installed

## Getting Started

Clone the repository and install the AWS SDK for Python:

```bash
git clone https://github.com/sudharsanbaskaran09-eng/aws-ai-projects-portfolio.git
cd aws-ai-projects-portfolio
pip install boto3
aws configure
```

Choose a project and follow its project-specific README for setup and usage instructions:

- [Project 1: Image Recognition](./project-1-image-recognition/README.md)
- [Project 2: Sentiment Analysis](./project-2-sentiment-analysis/README.md)

## Example Capabilities

### Image Recognition

Upload an image to Amazon S3 and use Amazon Rekognition to identify objects, scenes, and other labels with confidence scores.

### Sentiment Analysis

Submit text to Amazon Comprehend and receive sentiment classification with confidence scores for positive, negative, neutral, and mixed sentiment.

## Real-World Applications

These projects provide foundational patterns for building:

- E-commerce product tagging and review analysis
- Social media monitoring and content moderation
- Customer feedback and support-ticket classification
- Security and surveillance analysis workflows
- AI-powered serverless APIs

## Security and Cost Notes

- Follow the principle of least privilege when creating IAM roles and policies.
- Avoid storing AWS access keys in source code; use AWS CLI profiles, IAM roles, or environment-based credentials.
- Review S3 bucket permissions and enable encryption where appropriate.
- Monitor AWS usage and billing when experimenting with managed AI services.
- Remove unused resources after testing to avoid unexpected charges.

## Author

**Sudharsan Baskaran**

- LinkedIn: [sudharsan-baskaran-95443925a](https://linkedin.com/in/sudharsan-baskaran-95443925a)
- GitHub: [sudharsanbaskaran09-eng](https://github.com/sudharsanbaskaran09-eng)

## License

This repository is intended for learning and portfolio demonstration. Add a license file if you plan to distribute or reuse the code publicly.
