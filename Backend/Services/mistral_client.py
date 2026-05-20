""" Setting up Model : Mistral """
import os
from Backend.Config.settings import settings # API KEY
from Backend.Core.Features.LLmModelCore.llmService import llm_service_provider # LLM model
from mistralai.client.models import SystemMessage, UserMessage, AssistantMessage
from mistralai.client import Mistral


""" SETTING UP MISTRAL MODEL """ # TEMPLETE
class MODEL_MISTRAL:

    def __init__(self):
        
        # LOADING REQUIREMENTS
        self.API_KEY = settings.MISTRAL_API_KEY
        self.MISTRAL_MODEL_1 = llm_service_provider.MODEL_MISTRAL_1
        self.MISTRAL_MODEL_2 = llm_service_provider.MODEL_MISTRAL_2
        self.MEMORY_1 = []
        self.MEMORY_2 = []

        # LOADING SYSTEM PROMPT1
        root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
        prompt_path = os.path.join(root_dir, "Prompt", "codePrompt1.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
                self.prompt1 = f.read()

        # LOADING SYSTEM PROMPT2
        root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
        prompt_path = os.path.join(root_dir, "Prompt", "codePrompt2.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
                self.prompt2 = f.read()
    

    def mistralModel1(self, code1):
        
        # ADD USER INPUT TO MEMORY
        self.MEMORY_1.append(UserMessage(content=code1))

        # ADD SYSTEM PROMPT ONCE 
        if len(self.MEMORY_1) == 1:
             self.MEMORY_1.insert(0, SystemMessage(content=self.prompt1))

        # INITIALIZING CLIENT
        with Mistral(api_key=self.API_KEY) as mistral:
                completion_ = mistral.chat.complete(
                    model = self.MISTRAL_MODEL_1,
                    messages=self.MEMORY_1,          
                    stream=False)

        # Extract result
        result1 = completion_.choices[0].message.content

        # ADD ASSISTANT OUTPUT TO MEMORY
        self.MEMORY_1.append(AssistantMessage(content=result1))


        return result1

    def mistralModel2(self, code2):
          
        # ADD USER INPUT TO MEMORY
        self.MEMORY_2.append(UserMessage(content=code2))

        # ADD SYSTEM PROMPT ONCE 
        if len(self.MEMORY_2) == 1:
             
             self.MEMORY_2.insert(0, SystemMessage(content=self.prompt2))

        # INITIALIZING CLIENT
        with Mistral(api_key=self.API_KEY) as mistral:
                completion_ = mistral.chat.complete(
                    model = self.MISTRAL_MODEL_2,
                    messages=self.MEMORY_2,
                    stream=False)

        # Extract result
        result2 = completion_.choices[0].message.content

        # ADD ASSISTANT OUTPUT TO MEMORY
        self.MEMORY_2.append(AssistantMessage(content=result2))

        return result2
    
modelMistral = MODEL_MISTRAL()