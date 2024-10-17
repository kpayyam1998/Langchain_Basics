from langchain_openai import OpenAI

class OpenAIClient():
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm=None

    def _initiateClient(self):

        if not self.api_key:
            raise ValueError("API Key is required")
        
        self.llm = OpenAI(api_key=self.api_key)

    def _getllm(self):

        if not self.llm:
            self._initiateClient()
        
        return self.llm