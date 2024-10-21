import os
import requests
from langchain.llms.base import LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_ENDPOINT = os.getenv("LMSTUDIOAPI_URL")

# Custom LLM class for interacting with LM Studio API
class LMStudioLLM(LLM):
    def _call(self, prompt: str, stop=None) -> str:
        api_data = {
            "messages": [
                {"role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 50,
            "stream": False
        }

        response = requests.post(API_ENDPOINT, json=api_data, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            api_response = response.json()
            return api_response["choices"][0]["message"]["content"]
        else:
            raise ValueError(f"Error from LM Studio API: {response.status_code}, {response.text}")

    @property
    def _identifying_params(self):
        return {}

    @property
    def _llm_type(self):
        return "lm_studio"