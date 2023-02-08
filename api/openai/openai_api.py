import requests
import openai_config

def generate_response(prompt):
    headers = {
        "Authorization": "Bearer " + openai_config.api_key
    }
    data = {
        "model": "text-davinci-002",
        "prompt": prompt
    }

    response = requests.post("https://api.openai.com/v1/engines/davinci/jobs", headers=headers, json=data)
    response_text = response.json()["choices"][0]["text"]
    return response_text
