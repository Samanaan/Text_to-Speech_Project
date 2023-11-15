# Open ai import 
from openai import OpenAI
# open client OpenAI
client = OpenAI()

# audio file path (in future iterations this will be pulled from the website cache?)
audio_file= open("Test_audio.m4a", "rb")

#
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

print(transcript)
