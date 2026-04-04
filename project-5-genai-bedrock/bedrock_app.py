import boto3
import json

# Initialize Bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

# ✅ Use Nova Micro (stable + available)
MODEL_ID = "amazon.nova-micro-v1:0"


def generate_text(prompt):
    print(f"\n📝 Your Prompt: {prompt}")
    print("\n🤖 Generating AI response...")

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

        print("\n✅ AI Response:")
        print("-" * 50)
        print(generated_text)
        print("-" * 50)

        return generated_text

    except Exception as e:
        print("\n❌ ERROR:", str(e))
        return None


def save_response_to_file(prompt, response, filename):
    if response is None:
        print("⚠️ Skipping save due to error")
        return

    result = {
        "prompt": prompt,
        "response": response,
        "model": MODEL_ID
    }

    with open(filename, "w") as f:
        json.dump(result, f, indent=4)

    print(f"\n💾 Saved to {filename}")


# ---- MAIN ----
if __name__ == "__main__":

    prompt1 = "Explain what Amazon Web Services is in 3 sentences."
    response1 = generate_text(prompt1)
    save_response_to_file(prompt1, response1, "response1.json")

    prompt2 = "What is serverless computing and what are its main benefits?"
    response2 = generate_text(prompt2)
    save_response_to_file(prompt2, response2, "response2.json")

    prompt3 = "Write a short job description for an AWS Cloud AI Architect role."
    response3 = generate_text(prompt3)
    save_response_to_file(prompt3, response3, "response3.json")

    print("\n🎉 GenAI app complete! All responses saved.")
