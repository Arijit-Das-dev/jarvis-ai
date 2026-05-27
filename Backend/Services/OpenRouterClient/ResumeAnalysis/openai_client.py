import os
from Backend.Config.settings import settings # API KEY
from Backend.Core.Features.LLmModelCore.llmService import llm_service_provider # LLM 
from openrouter import OpenRouter

class MODEL_GPT:

    def __init__(self):
        
        self.API_KEY = settings.GPT_API_KEY
        self.MODEL = llm_service_provider.MODEL_GPT

        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
        prompt_path = os.path.join(root_dir, "Prompt", "gptPrompt.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
    
    def askGpt(self, content, role):

        final_query = f"""User resume content : {content} \n Prompt : {self.system_prompt} \n User job role :{role}"""

        with OpenRouter(api_key=settings.GPT_API_KEY) as client:

            response = client.chat.send(
                model=self.MODEL,
                messages=[
                    {
                        "role":"user",
                        "content":final_query
                    }
                ] 
            )

        result = response.choices[0].message.content
        return result