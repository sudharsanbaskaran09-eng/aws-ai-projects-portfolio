import boto3
import json

s3_client = boto3.client('s3', region_name='us-east-1')
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

BUCKET_NAME = 'rag-documents-brat'
MODEL_ID = 'amazon.nova-lite-v1:0'

def load_knowledge_base():
    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key='documents/knowledge_base.txt'
    )
    return response['Body'].read().decode('utf-8')

def split_into_chunks(text):
    paragraphs = text.split('\n\n')
    return [p.strip() for p in paragraphs if p.strip()]

def find_relevant_chunks(question, chunks, top_k=3):
    question_words = set(question.lower().split())
    scored_chunks = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        overlap = len(question_words.intersection(chunk_words))
        scored_chunks.append((overlap, chunk))
    scored_chunks.sort(reverse=True)
    relevant = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]
    return relevant if relevant else [chunks[0]]

def generate_answer(question, context):
    prompt = f"""You are a helpful AWS knowledge assistant.
Use only the following context to answer the question.
If the answer is not in the context say I do not have that information.

Context:
{context}

Question: {question}

Answer:"""

    request_body = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 512,
            "temperature": 0.3
        }
    }

    response = bedrock_client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(request_body),
        contentType='application/json',
        accept='application/json'
    )

    response_body = json.loads(response['body'].read())
    return response_body['output']['message']['content'][0]['text']

def lambda_handler(event, context):
    if isinstance(event.get('body'), str):
        body = json.loads(event['body'])
    else:
        body = event

    question = body.get('question', '')

    if not question:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Question is required'})
        }

    knowledge_base = load_knowledge_base()
    chunks = split_into_chunks(knowledge_base)
    relevant_chunks = find_relevant_chunks(question, chunks)
    context_text = '\n\n'.join(relevant_chunks)
    answer = generate_answer(question, context_text)

    return {
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

