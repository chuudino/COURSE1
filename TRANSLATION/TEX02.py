# pip install pydub
# pip install SpeechRecognition
# pip install pyaudio
import requests
import os
import sys
from pydub import AudioSegment
import speech_recognition as sr


############################定義函式############################
def convert_m4a_to_wav(input_file, output_file):
    # 讀取 M4A 檔案
    audio = AudioSegment.from_file(input_file, format="m4a")
    # 儲存為 WAV 格式
    audio.export(output_file, format="wav")
    print(f"轉檔完成：{output_file}")


############################ 主程式 #################################
convert_m4a_to_wav(
    "d:/小會研發組2023/audio20241119 錄音檔.m4a",
    "d:/小會研發組2023/audio20241119 錄音檔.wav",
)
# 初始化辨識器
recognizer = sr.Recognizer()
# 載入 WAV 檔案
with sr.AudioFile("d:/小會研發組2023/audio20241119 錄音檔.wav") as source:
    audio_data = recognizer.record(source)  # 讀取整個音訊檔案
# 語音轉文字
try:
    text = recognizer.recognize_google(audio_data, language="zh-TW")
    # 使用 Google API (可選中文)
    print("轉錄文字內容：", text)
except sr.UnknownValueError:
    print("無法辨識音訊內容")
except sr.RequestError as e:
    print(f"API 請求錯誤: {e}")
