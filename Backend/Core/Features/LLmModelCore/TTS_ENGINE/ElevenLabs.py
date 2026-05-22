from elevenlabs.client import ElevenLabs
from Backend.Config.settings import settings
from Backend.Core.Features.LLmModelCore.llmService import elevenlabs_tts_model_provider
from elevenlabs.play import play

def playAudio(content: str):

    client = ElevenLabs(
        api_key=settings.ELEVENLABS_API_KEY
    )

    audio = client.text_to_speech.convert(
        text=content,
        voice_id=elevenlabs_tts_model_provider.ELEVENLABS_VOICE_ID,
        model_id=elevenlabs_tts_model_provider.ELEVENLABS_MODEL_ID,
        output_format=elevenlabs_tts_model_provider.ELEVENLABS_OUTPUT_FORMAT_ID
    )

    startAudio = play(audio)

    return startAudio