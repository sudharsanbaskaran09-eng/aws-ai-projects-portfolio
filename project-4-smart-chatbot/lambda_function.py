'ChatHistory'

# Chatbot responses
RESPONSES = {
    'hello': 'Hello! Welcome! How can I help you today?',
    'hi': 'Hi there! How can I assist y
    'price': 'AWS offers a Free Tier for most services. Visit aws.amazon.com/free for details.',
    'default': 'I did not understand that. Try asking about: aws, services, contact, github or help.'
}

def get_response(user_message):
    """Generate chatbot response based on user input"""
    message_lower = user_message.lower().strip()

    return RESPONSES['default']

def save_to_dynamodb(session_id, user_message, bot_response):
    """Save conversation to DynamoDB"""
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'user_message': user_message,
            'bot_response': bot_respo
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

