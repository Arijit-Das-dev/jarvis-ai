import os
import cohere
from Backend.Config.settings import settings # cohere api key
from Backend.Core.Features.LLmModelCore.llmService import llm_service_provider # cohere model

""" SETTING UP COHERE MODEL """
class MODEL_COHERE:

    def __init__(self):
        
        self.MODEL = llm_service_provider.MODEL_COHERE # BACKEND/CORE/FEATURES/LLMMODELCORE/LLMSERVICE
        self.CLIENT = cohere.ClientV2(api_key=settings.COHERE_API_KEY) # BACKEND/CONFIG/SETTINGS
        self.MEMORY = []

        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        prompt_path = os.path.join(root_dir, "Prompt", "coherePrompt.txt")

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def askCohere(self, user_input, context):
        
         # Memory control (last 2 turns)
        MAX_TURNS = 2
        self.MEMORY = self.MEMORY[-(MAX_TURNS * 2):]
        
        messages = [
            {
                "role":"system",
                "content":self.system_prompt
            },
            {
                "role":"system",
                "content": f"Context:\n{context}"
            },
            *self.MEMORY,
            {
                "role":"user",
                "content":user_input
            }
        ]

        response = self.CLIENT.chat(
            model=self.MODEL,
            messages=messages,
            temperature=0.3
        )

        reply = response.message.content[0].text

        # updated memory
        self.MEMORY.append(
            {
                "role":"user",
                "content":user_input
            },
        )

        self.MEMORY.append(
            {
                "role":"assistant",
                "content":reply
            }
        )

        return reply