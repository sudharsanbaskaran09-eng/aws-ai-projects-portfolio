# Smart Chatbot — AWS AI Project

## Overview
A serverless AI chatbot built on AWS that handles real conversations,
generates intelligent responses and permanently stores every chat
in DynamoDB. Accessible via a REST API from any platform or application.

## Architecture
User → API Gateway → Lambda → DynamoDB

## AWS Services Used

| Service | Purpose |
|---------|---------|
| AWS Lambda | Serverless chatbot brain and response logic |
| Amazon API Gateway | REST API endpoint exposure |
| Amazon DynamoDB | Permanent chat history storage |
| AWS IAM | Security, roles and permissions |

## Real World Use Cases
- Customer support automation for websites
- FAQ bots for mobile and web apps
- HR onboarding assistant
- E-commerce product inquiry bot

## Project Structure

```

project-4-smart-chatbot/
├── lambda_function.py       # Chatbot brain — Lambda handler
├── chatbot_client.py        # Local Python chat client
├── README.md
└── screenshots/

```

## Prerequisites
- AWS Account with Free Tier
- Python 3.x
- AWS CLI configured
- requests library installed

## How to Run

### Local Chat Client
```bash
pip install requests
python chatbot_client.py
```

### API
```powershell
Invoke-WebRequest -Uri "https://your-api-url/prod/chat" `
-Method POST `
-Headers @{"Content-Type"="application/json"} `
-Body '{"message": "Hello", "session_id": "user-001"}'
```

## Sample Output
```json
{
    "session_id": "abc-123",
    "user_message": "Hello",
    "bot_response": "Hello! Welcome to AWS AI Chatbot! How can I help you today?",
    "timestamp": "2026-03-29T10:30:00"
}
```

## Author
Sudharsan Baskaran
- LinkedIn: https://linkedin.com/in/sudharsan-baskaran-95443925a
- GitHub: https://github.com/sudharsanbaskaran09-eng
