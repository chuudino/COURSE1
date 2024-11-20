# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
import requests
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
from google.cloud import speech_v1 as speech
import assemblyai as aai

client = speech.SpeechClient()

############################設定工作目錄############################
os.chdir(sys.path[0])

############################定義常數############################
API_KEY = "a97083c222204f62810bc7a9694cb583"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"


############################ 設定音訊檔案 #################################
audio = {"uri": "gs://YOUR_BUCKET_NAME/YOUR_AUDIO_FILE.flac"}
config = {
    "encoding": "FLAC",
    "sample_rate_hertz": 16000,
    "language_code": "zh_tw",
}


aai.settings.api_key = 
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)

response = client.recognize(config=config, audio=audio)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
