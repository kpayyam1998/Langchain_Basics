#from langchain.chains import LLMChain

class ChainExcutor:
    def __init__(self,llm,prompt_template) -> None:
        self.llm = llm
        self.prompt_template = prompt_template

    def runChain(self,country):
        # Check llm and prompt_template present or not
        if not self.llm or not self.prompt_template:
            raise ValueError("LLM and Prompt Template must be provided")
        chain = self.prompt_template | self.llm

        response = chain.invoke({
            "country": country
        })

        # Check if response is present or not
        if not response:
            raise ValueError("No response from the LLM")
        # Process the response as needed
        return response
