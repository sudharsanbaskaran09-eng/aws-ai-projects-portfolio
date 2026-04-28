import requests
import uuid
import json
        result = response.json()

        # API Gateway usually wraps response in 'body'
        body = json.loads(result.get('body', '{}'))

        return body.get('bot_response', "No response from bo

    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"
    except json.JSONDecodeError:
        return "Error parsing response from server"

# ---- MAIN PROGRAM ----
print("=" * 50)
print("AWS Smart Chatbot — Lambda + DynamoDB")
print("=" * 50)
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Bot: Goodbye! Chat history saved to DynamoDB!")
        break

    response = chat(user_input)
    print(f"Bot: {response}\n")
