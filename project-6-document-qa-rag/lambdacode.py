import boto3
import json
    r
    }

    response = bedrock_client.invoke_model')

    if not question:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Question is required'})
        
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'question': question,
            'answer': answer,
            'chunks_used': len(relevant_chunks),
            'model': MODEL_ID
        })
    }

