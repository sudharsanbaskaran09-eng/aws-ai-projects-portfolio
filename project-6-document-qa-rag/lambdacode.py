import boto3
import json
    r
    }

    response = bedrock_client.invoke_model')

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

