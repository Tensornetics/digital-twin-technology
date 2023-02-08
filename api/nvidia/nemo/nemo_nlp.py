import requests


class NemoNLP:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nvidia.com/nemo/v1/models/nlp"

    def process_text(self, text):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "input_text": text
        }
        response = requests.post(
            f"{self.base_url}/process", headers=headers, json=data)
        response_json = response.json()
        return response_json
