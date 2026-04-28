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



    response = chat(user_input)
    print(f"Bot: {response}\n")
