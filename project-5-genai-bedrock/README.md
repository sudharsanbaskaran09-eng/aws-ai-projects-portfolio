# GenAI App with Amazon Bedrock — AWS AI Project

## Overview
A serverless Generative AI application built on AWS that accepts any
text prompt and returns AI-generated responses using Amazon Bedrock
and the Amazon Titan foundation model. Exposed via a REST API and
ity, roles and permissions |

## Real World Use Cases
- AI content generation for marketing teams
- Automated report and summary generation
- Customer support response drafting
- Code explanation and documentation generation

## Project Structure

```

project-5-genai-bedrock/
├── bedrock_app.py           # Local script for GenAI testing
├── lambda_function.py       # Lambda handler for serverless execution
├── response1.json           # Sample AI output — general knowledge
├── response2.json           # Sample AI output — technical question
├── response3.json           # Sample AI output — creative use case
├── README.md
└── screenshots/

```

## Prerequisites
- AWS Account with Free Tier
- Amazon Bedrock model access enabled for Titan
- Python 3.x
- AWS CLI configured
- boto3 installed

## How to Run

### Local
```bash
pip install boto3
aws configure
python bedrock_app.py

```

### API
```powershell
Invoke-WebRequest -Uri "https://8hknovmphb.execute-api.us-east-1.amazonaws.com/prod/generate" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"prompt": "Your prompt here"}'

```

###Sample Output
```json
{
    "prompt": "Explain what Amazon Web Services is in 3 sentences.",
    "response": "Amazon Web Services (AWS) is a cloud computing platform that provides on-demand access to computing resources such as servers, storage, and databases over the internet. It allows businesses to scale applications without managing physical infrastructure and pay only for what they use. AWS is widely used by startups and enterprises to build, deploy, and manage applications efficiently.",
    "model": "amazon.nova-micro-v1:0"
}

```

## Author
Sudharsan Baskaran
- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
