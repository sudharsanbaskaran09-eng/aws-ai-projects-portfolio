import boto3
import json

# Initialize Bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

# Model ID
MODEL_ID = "amazon.nova-micro-v1:0"


def lambda_handler(event, context):

    # Handle API Gateway input
    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event

    prompt = body.get('prompt', '')

    if not prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Prompt is required'})
        }

    try:
        response = bedrock_client.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            inferenceConfig={
                "maxTokens": 512,
                "temperature": 0.7,
                "topP": 0.9
            }
        )

        generated_text = response['output']['message']['content'][0]['text']

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'prompt': prompt,
                'response': generated_text,
                'model': MODEL_ID
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
