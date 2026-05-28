from Backend.Core.Features.LLmModelCore.TTS_ENGINE.elevenlabs_client import playAudio

if __name__ == "__main__":

    text = "Hello there !"
    playAudio(content=text)