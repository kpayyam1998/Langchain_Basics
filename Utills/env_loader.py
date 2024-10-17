import os 
from dotenv import load_dotenv

class EnvLoader:
    def __init__(self):
        load_dotenv()

    def get_api_key(self):

        key=os.getenv("OPENAI_API_KEY")
        if key is None:
            raise ValueError("OPENAI_API_Key wasnot present")
        return key