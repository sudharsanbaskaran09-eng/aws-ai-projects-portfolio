import boto3

    print("📚 Loading knowledge base from S3...")
    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key='documents/knowledge_base.txt'
    )
    content = response['Body'].read().decode('utf-8')
    print(f"✅ Knowledge base(text, chunk_size=400):
    """Split document into smaller chunks"""
    paragraphs = text.split('\n\n')
    chunks = []
        if para.strip():
            chunks.append(para.strip())
    print(f"📄 Document split into {len(chunks)} chunks")
    return chunks

def find_relevant_chunks(question, chunks, top_k=3):
    """Find most relevant chunks using keyword matching"""
    question_words = set(question.lower().split())
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        overlap = len(question_words.intersection(chunk_words))
        scored_chunks.append((overlap, chunk))

    scored_chunks.sort(reverse=True)
    relevant = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    if not relevant:
        relevant = [chunks[0]]

    return relevant

def generate_answer(question, context):
    """Send question + context to Bedrock Nova Lite"""
    prompt = f"""You are a helpful AWS knowledge assistant.
Use only the following context to answer the question.
If the answer is not in the context say I do not have that information.

Context:
{context}

Question: {question}

Answer:"""

    # Nova Lite uses Messages API format
    request_body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
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

def answer_question(question):
    """Full RAG pipeline — retrieve then generate"""
    print(f"\n❓ Question: {question}")
    print("🔍 Searching knowledge base...")

    knowledge_base = load_knowledge_base()
    chunks = split_into_chunks(knowledge_base)
    relevant_chunks = find_relevant_chunks(question, chunks)
    context = '\n\n'.join(relevant_chunks)

    print(f"✅ Found {len(relevant_chunks)} relevant sections")
    print("🤖 Generating answer with Amazon Nova Lite...")

    answer = generate_answer(question, context)

    print("\n💡 Answer:")
    print("-" * 50)
    print(answer)
    print("-" * 50)

    return answer

# ---- MAIN ----
if __name__ == "__main__":
    questions = [
        "What is Amazon Bedrock?",
        "What is RAG and how does it work?",
        "What does a Cloud AI Architect do?",
        "What is AWS Lambda used for?",
        "What is Amazon Textract?"
    ]

    print("=" * 60)
    print("AWS Document Q&A Bot — RAG Architecture")
    print("Powered by Amazon Nova Lite + S3")
    print("=" * 60)

    for question in questions:
        answer_question(question)
        print()

    print("🎉 RAG Q&A Bot complete!")
