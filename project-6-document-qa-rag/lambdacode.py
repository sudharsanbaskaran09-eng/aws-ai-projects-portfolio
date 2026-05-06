import boto3
import json

    response_body = json.loads(response['body'].read())
    return response_body['output']['message']['content'][0]['text']

    question = body.get('question', '')

    if not question:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Question is required'})
        }

    knowledge_base = load_knowledge_base()
   
            'model': MODEL_ID
        })
    }




























