from langchain_core.prompts import PromptTemplate

class PromptManager:
    def __init__(self):
        self.prompt_template =None

    def create_template(self):
        self.prompt_template = PromptTemplate(
            input_variables=["country"],
            template="Who is the president of {country} in 2010?"
        )

    def get_template(self):       
        if not self.prompt_template:
            self.create_template()
        
        return self.prompt_template
