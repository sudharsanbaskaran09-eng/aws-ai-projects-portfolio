import boto3
import json

comprehend_client = boto3.client('comprehend')

def lambda_handler(event, context):

    # Handle both direct and API Gateway requests
    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event

    text = body['text']

    # Call Comprehend
    response = comprehend_client.detect_sentiment(
        Text=text,
        Lang

    sentiment = response['Sentiment']
    scores = response['SentimentScore']

    ret
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'sentiment': sentiment,
            'scores': {
                'Positive': round(scores['Positive'], 4),
                'Negative': round(scores['Negative'], 4),
                'Neutral': round(scores['Neutral'], 4),
                'Mixed': round(scores['Mixed'], 4)
            },
            'message': f'Text sentiment is {sentiment}'
        })
    }
