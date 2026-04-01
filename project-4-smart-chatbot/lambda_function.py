import boto3
import json
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'ChatHistory'

# Chatbot responses
RESPONSES = {
    'hello': 'Hello! Welcome! How can I help you today?',
    'hi': 'Hi there! How can I assist you?',
    'help': 'I can help you with: 1) AWS Services 2) Project Info 3) Contact Details. What do you need?',
    'aws': 'AWS offers 200+ cloud services including AI, compute, storage and databases. What would you like to know?',
    'services': 'Our key services are: Image Recognition, Sentiment Analysis, Document Scanner and Smart Chatbot.',
    'contact': 'You can reach us at: sudharsan@example.com or visit our GitHub portfolio.',
    'github': 'Check out our AWS AI Projects Portfolio on GitHub: github.com/sudharsanbaskaran09-eng',
    'bye': 'Goodbye! Have a great day!',
    'thanks': 'You are welcome! Is there anything else I can help you with?',
    'price': 'AWS offers a Free Tier for most services. Visit aws.amazon.com/free for details.',
    'default': 'I did not understand that. Try asking about: aws, services, contact, github or help.'
}

def get_response(user_message):
    """Generate chatbot response based on user input"""
    message_lower = user_message.lower().strip()

    for keyword, response in RESPONSES.items():
        if keyword in message_lower:
            return response

    return RESPONSES['default']

def save_to_dynamodb(session_id, user_message, bot_response):
    """Save conversation to DynamoDB"""
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'user_message': user_message,
            'bot_response': bot_response
        }
    )

def lambda_handler(event, context):

    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event

    user_message = body.get('message', '')
    session_id = body.get('session_id', str(uuid.uuid4()))

    if not user_message:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Message is required'})
        }

    # Get bot response
    bot_response = get_response(user_message)

    # Save to DynamoDB
    save_to_dynamodb(session_id, user_message, bot_response)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'session_id': session_id,
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
    }
