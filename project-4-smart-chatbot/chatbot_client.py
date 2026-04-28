import requests
import uuid
import json
        result = response.json()

        # API Gateway usually wraps response in 'body'
        body = json.loads(result.get('body', '{}'))

        return body.get('bot_response', "No response from bo

    except requests.exceptions.RequestException as e:
        return f"Error connectin
