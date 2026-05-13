""" Setting up model : GEMINI """

from Backend.Config.settings import settings
from Backend.Core.Features.LLmModelCore.llmService import llm_service_provider
from google import generativeai as genai
from google.generativeai import types
import os


""" SETTING UP GEMINI MODEL """ # TEMPLETE
class MODEL_GEMINI:

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

    def askGemini(self, query):

        userMessage = types.Content(
            role="user",
            parts = [types.Part.from_text(text=query)]
        )
        self.memory.append(userMessage)

        try:
            response = self.client.models.generate_content(
                model=self.Model,
                contents=self.memory,
                config=types.GenerateContentConfig(
                    system_instruction=self.system_prompt,
                    temperature=0.7,  # Higher = more creative, Lower = more factual
                    max_output_tokens=1000,
                )
            )
            result = response.text

            modelMessage = types.Content(
                role="model",
                parts=[types.Part.from_text(text=result)]
            )

            self.memory.append(modelMessage)

            return result

        except Exception as e:
            return f"An error occurred: {str(e)}"

modelGemini = MODEL_GEMINI()