import whisper
import subprocess

# Load the Whisper model
model = whisper.load_model("large-v3")

# Transcribe the audio
result = model.transcribe("00002.wav")
print(result)
#print(result['text'])
