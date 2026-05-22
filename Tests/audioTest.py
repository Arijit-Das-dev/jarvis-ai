from Backend.Core.Features.LLmModelCore.TTS_ENGINE.ElevenLabs import playAudio

if __name__ == "__main__":

    text = "Hello there !"
    playAudio(content=text)