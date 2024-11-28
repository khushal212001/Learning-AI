import requests
import json
import sseclient
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv('API_KEY')

def performRequestWithStreaming():
    reqUrl = 'https://api.openai.com/v1/completions'
    reqHeaders = { 
        'Accept': 'text/event-stream',
        'Authorization': 'Bearer ' + api_key
    }

    reqBody = {
        "model": "gpt-3.5-turbo-instruct",  # Correct model
        "prompt": "What is Python?",  # Chat prompt
        
        "max_tokens": 100,
        "temperature": 0,
        "stream": True,
    }
    # Print request details
    print("Sending request to OpenAI API...")
    print(f"URL: {reqUrl}")
    print(f"Headers: {reqHeaders}")
    print(f"Body: {reqBody}")

    request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)

    # Check the response status
    print(f"Response status code: {request.status_code}")
    if request.status_code != 200:
        print(f"Error: {request.text}")
        return

    client = sseclient.SSEClient(request)
    str=""
    for event in client.events():
        if event.data != '[DONE]':

            # eventData=event.data
            # print(f"{event.data}")
            data = json.loads(event.data)
            choices=data['choices']
            # print(f"{choices}")
            
            if choices:  # Ensure choices list is not empty
                text = choices[0]['text']
                str+=text
            else:
                print("No choices found")
            # print(json.loads(event.data)['choices'][0]['text'], end="", flush=True)
        else:
            print("Received [DONE] event")
            break
    print(str)

if __name__ == '__main__':
    performRequestWithStreaming()
