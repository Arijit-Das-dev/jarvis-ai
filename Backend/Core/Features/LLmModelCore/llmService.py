# Storing LLM models => LLaMa, Mistral, Gemini

import yaml

# AI MODEL (GENERATIVE AI MODELS)
class LLM_SERVICE_PROVIDER:

    with open("Backend/Config/models.yaml", "r") as file:
        CONFIG = yaml.safe_load(file)

    MODEL_LLAMA = CONFIG["LLM_MODELS"]["LLAMA"]["modelName"]
    MODEL_MISTRAL_1 = CONFIG["LLM_MODELS"]["MISTRAL"]["mistral_1"]
    MODEL_MISTRAL_2 = CONFIG["LLM_MODELS"]["MISTRAL"]["mistral_2"]
    MODEL_GEMINI = CONFIG["LLM_MODELS"]["GEMINI"]["gemini"]
    MODEL_COHERE = CONFIG["LLM_MODELS"]["COHERE"]["cohere"]
    MODEL_COHERE2 = CONFIG["LLM_MODELS"]["COHERE"]["cohere2"]
    MODEL_GPT = CONFIG["LLM_MODELS"]["OPEN_ROUTER"]["GPT"]
    
# EMBEDDING MODELS BY HUGGINGFACE
class EMBEDDING_MODEL_PROVIDER():

   with open("Backend/Config/models.yaml", "r") as file:
        CONFIG = yaml.safe_load(file)

   HUGGING_FACE_MODEL = CONFIG["EMBEDDING_MODELS"]["Huggingface"]["huggingface_model"]

embedding_model_provider = EMBEDDING_MODEL_PROVIDER()
llm_service_provider = LLM_SERVICE_PROVIDER()