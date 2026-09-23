""" Setting up model : GEMINI """

from Backend.Config.settings import settings
from Backend.Core.Features.LLmModelCore.llm_Service import llm_service_provider
import google.generativeai as genai
from google.generativeai import types
import os


""" SETTING UP GEMINI MODEL """ # TEMPLETE
class MODEL_GEMINI:

    MAX_TURNS = 5

    def __init__(self):
        
        # Model Configuration
        self.Model = llm_service_provider.MODEL_GEMINI
        self.API_KEY = settings.GEMINI_API_KEY
        self.memory = []
        self.client = genai.Client(api_key=self.API_KEY)

        # Prompt
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        prompt_path = os.path.join(root_dir, "Prompt", "PromptEng.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def _trim_memory(self):

        max_messages = self.MAX_TURNS * 2 # 10
        if len(self.memory) > max_messages: # check if messages hit the length of 10 
            self.memory = self.memory[-(max_messages):] # keep 10 last conversation

    def askGemini(self, query):

        userMessage = types.Content(
            role="user",
            parts = [types.Part.from_text(text=query)]
        )
        self.memory.append(userMessage)

        # trim old history
        self._trim_memory()

        conversaton = [

            # System Prompt
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=self.system_prompt
                    )
                ]
            )
        ] + self.memory

        try:
            response = self.client.models.generate_content(
                model=self.Model,
                contents=conversaton
            )
            result = response.text

            # Save Assistant Response
            assistant_message = types.Content(
                role="model",
                parts=[
                    types.Part.from_text(text=result)
                ]
            )

            self.memory.append(assistant_message)

            # Trim again after assistant response
            self._trim_memory()

            return result

        except Exception as e:
            return f"An error occurred: {str(e)}"

modelGemini = MODEL_GEMINI()