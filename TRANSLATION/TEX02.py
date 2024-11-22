import os
import sys
from pydub import AudioSegment
import whisper

# 設定工作目錄為當前腳本所在位置
os.chdir(sys.path[0])


############################ 定義函式 ############################
def convert_and_trim_m4a(input_file, output_file, duration_ms):
    """將 M4A 檔案轉換為 WAV 並切割到指定時間"""
    # 讀取 M4A 檔案
    audio = AudioSegment.from_file(input_file, format="m4a")

    # 切割到指定時間（毫秒）
    trimmed_audio = audio[:duration_ms]

    # 儲存為 WAV 格式
    trimmed_audio.export(output_file, format="wav")
    print(f"音訊切割並轉檔完成：{output_file}")


def transcribe_with_whisper(audio_file):
    """使用 OpenAI Whisper 進行語音轉文字"""
    model = whisper.load_model("medium")  # 選擇模型
    result = model.transcribe(audio_file)
    print("轉錄結果：")
    print(result["text"])
    return result["text"]


############################ 主程式 ############################
# 定義檔案路徑
org_path = "D:\\小會研發組2023\\audio20241119 錄音檔.m4a"
one_min_path = "audio20241119_trimmed.wav"
duration_ms = 60 * 1000  # 切割為 1 分鐘（60 秒）

# 第一步：將 M4A 檔案切割並轉換為 WAV
# convert_and_trim_m4a(input_m4a, output_wav, duration_ms)

# 第二步：使用 Whisper 將 WAV 檔案轉換為文字
result = transcribe_with_whisper(one_min_path)

# 第三步：將文字存到 TXT 檔案
with open("audio20241119.txt", "w", encoding="utf-8") as f:
    f.write(result)  # 將文字寫入 TXT 檔案
