from Backend.Core.Features.LLmModelCore.tts_engine.elevenlabs_client import playAudio

if __name__ == "__main__":

    text = "Hello there !"
    playAudio(content=text)