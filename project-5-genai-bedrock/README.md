
- Customer support response drafti```

project-5-genai-bedrock/
├── bed
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

