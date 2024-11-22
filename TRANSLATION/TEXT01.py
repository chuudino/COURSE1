# pip install SpeechRecognition
# pip install pyaudio
import requests
import os
import sys

# import speech
import speech_recognition as sr

############################設定工作目錄############################
os.chdir(sys.path[0])


############################定義函式############################
def audio_to_text(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="zh-TW")
        print("轉譯結果:", text)
    except sr.UnknownValueError:
        print("無法辨識語音")
    except sr.RequestError as e:
        print(f"API 請求失敗: {e}")


############################ 設定音訊檔案 #################################
audio_to_text("d:/小會研發組2023/audio20241119 錄音檔.m4a")
