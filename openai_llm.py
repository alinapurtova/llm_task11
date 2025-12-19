import os
from dotenv import load_dotenv
from openai import OpenAI
from deepeval.models import DeepEvalBaseLLM

load_dotenv()

class OpenAILLM(DeepEvalBaseLLM):
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_model_name(self):
        return self.model

    def load_model(self):
        pass

    def generate(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    async def a_generate(self, prompt: str):
        return self.generate(prompt)
