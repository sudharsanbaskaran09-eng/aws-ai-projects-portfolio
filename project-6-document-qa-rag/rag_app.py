import boto3

    print("📚 Loading knowledge base from S3...")
    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key='documents/knowledge_base.txt'
  
        chunk_words = set(chunk.lower().split())
        overlap = len(question_words.intersection(chunk_words))
        scored_chunks.append((overlap, chunk))

    scored_chunks.sort(reverse=True)
    relevant = [chunk for score, chunk in scored_chunks[:top_k] if score > 0]

    if not relevant:
        relevant = [chunks[0]]

    return relevant


Answer:"""

    # No

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
