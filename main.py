from Utills.env_loader import EnvLoader
from Src.ChainExcutor.chain_excutor import ChainExcutor
from Src.OpenAI.openai_client import OpenAIClient
from Src.PromptConnect.promptmanager import PromptManager

class Main:
    def __init__(self):

        #Load Environment Variables
        self.env_loader = EnvLoader()

        # Initialize prompt and OpenAI 
        self.prompt_manager = PromptManager()
        self.api_key = self.env_loader.get_api_key()
        self.openai_client = OpenAIClient(api_key=self.api_key)

    def run(self, country : str) -> str:

        # Get PromptTemplate
        if not country:
            raise ValueError("Country is required")
        
        prompt_template = self.prompt_manager.get_template()

        if not prompt_template:
            raise ValueError("No prompt template found")
        
        # OpenAI client
        llm = self.openai_client._getllm()

        # Chain
        chain_excutor = ChainExcutor(llm, prompt_template)
        response = chain_excutor.runChain(country)

        return response
    
if __name__ == "__main__":
    # Main Program object
    program = Main()

    # Country
    country = "USA"

    result = program.run(country)

    # Output
    print(result)