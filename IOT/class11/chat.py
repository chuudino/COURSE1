"""
IoT 智慧家居 AI 對話助理
使用 OpenAI Chat Completions API + gpt-5.1-chat-latest 模型
透過 MQTT 發送指令給 MCU 控制設備
支援鍵盤打字 & 麥克風語音輸入
"""

from openai import OpenAI
import paho.mqtt.client as mqtt
import speech_recognition as sr
import os
from dotenv import load_dotenv

# 載入腳本同目錄下的 .env（不依賴工作目錄）
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# ============================================================
# OpenAI 設定
# ============================================================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "gpt-5.1-chat-latest"

# ============================================================
# 系統提示 (Developer Message) — 遵循最佳實踐
# ============================================================
# 最佳實踐原則：
#   1. 使用 developer role (instructions 參數)，優先級高於 user 訊息
#   2. 明確定義角色與唯一職責
#   3. 嚴格約束輸出格式 — 只能輸出指令字串，禁止任何多餘文字
#   4. 列舉所有合法指令與語義
#   5. 使用 XML delimiter 區分提示結構
#   6. 提供 few-shot 範例強化格式約束
#   7. 明確邊界處理（無關輸入回覆 NONE）
# ============================================================

SYSTEM_PROMPT = """
<role>
你是一個智慧家居 IoT 控制器。你的唯一職責是根據使用者描述的家中狀況，輸出對應的設備控制指令。
</role>

<rules>
- 你的回覆只能包含一個指令字串，不得包含任何其他文字、解釋、標點符號、空格或換行。
- 合法指令只有以下五個：ON、OFF、AUTO、PLAY、NONE
- 嚴格禁止輸出任何不在上述列表中的內容。
</rules>

<commands>
ON  → 開燈（全白光），適用於使用者反映環境太暗、需要照明的情境
OFF → 關燈，適用於使用者反映要離開、睡覺、不需要燈光的情境
AUTO → 自動根據環境光感測器調整亮度，適用於使用者希望燈光自動調節的情境
PLAY → 播放音樂，適用於使用者想聽音樂、想放鬆、想要背景音樂的情境
NONE → 不需要任何操作，適用於使用者的描述與設備控制無關的情境
</commands>

<examples>
使用者：家裡好暗 → ON
使用者：太暗了看不到 → ON
使用者：開燈 → ON
使用者：我要出門了 → OFF
使用者：關燈吧 → OFF
使用者：要睡覺了 → OFF
使用者：讓燈光自動調整 → AUTO
使用者：幫我根據環境亮度調光 → AUTO
使用者：播一首歌 → PLAY
使用者：我想聽音樂 → PLAY
使用者：今天天氣真好 → NONE
使用者：你好嗎 → NONE
</examples>
""".strip()

# ============================================================
# MQTT 設定
# ============================================================
MQTT_BROKER = "mqtt.singularinnovation-ai.com"
MQTT_PORT = 1883
MQTT_USER = "singular"
MQTT_PASSWORD = "Singular#1234"
MQTT_TOPIC = "dino"  # 對應 MCU main.py 訂閱的主題

# 合法指令集合
VALID_COMMANDS = {"ON", "OFF", "AUTO", "PLAY"}


def setup_mqtt():
    """建立並回傳 MQTT 客戶端"""
    mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()  # 啟動背景執行緒處理網路事件
    print(f"[MQTT] 已連線到 {MQTT_BROKER}:{MQTT_PORT}")
    return mqtt_client


def ask_ai(user_input):
    """
    呼叫 OpenAI Chat Completions API，取得 AI 回覆的指令字串
    使用 system role 傳入開發者級別系統提示
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content.strip().upper()


# ============================================================
# 語音辨識設定
# ============================================================
recognizer = sr.Recognizer()


def listen_microphone():
    """
    使用麥克風收音並透過 Google Speech Recognition 辨識為中文文字。
    回傳辨識結果字串，失敗時回傳 None。
    """
    with sr.Microphone() as source:
        print("[麥克風] 調整環境噪音中...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("[麥克風] 請說話... (最長 10 秒)")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("[麥克風] 超時，未偵測到語音")
            return None

    print("[麥克風] 辨識中...")
    try:
        text = recognizer.recognize_google(audio, language="zh-TW")
        print(f"[語音辨識] 你說了: {text}")
        return text
    except sr.UnknownValueError:
        print("[麥克風] 無法辨識語音，請再試一次")
        return None
    except sr.RequestError as e:
        print(f"[麥克風] 語音辨識服務錯誤: {e}")
        return None


def main():
    print("=" * 50)
    print("  智慧家居 AI 對話助理")
    print(f"  模型: {MODEL}")
    print(f"  MQTT Topic: {MQTT_TOPIC}")
    print("  輸入文字 → 打字控制")
    print("  直接按 Enter → 語音控制")
    print("  輸入 'exit' 或 'quit' 結束程式")
    print("=" * 50)

    # 建立 MQTT 連線
    mqtt_client = setup_mqtt()

    while True:
        try:
            user_input = input("\n你 (打字 / 按 Enter 說話): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再見！")
            break

        # 直接按 Enter → 啟動麥克風語音輸入
        if not user_input:
            user_input = listen_microphone()
            if not user_input:
                continue

        if user_input.lower() in ("exit", "quit"):
            print("再見！")
            break

        # 呼叫 AI 取得指令
        try:
            command = ask_ai(user_input)
        except Exception as e:
            print(f"[錯誤] AI 呼叫失敗: {e}")
            continue

        print(f"AI: {command}")

        # 判斷並發送 MQTT 指令
        if command in VALID_COMMANDS:
            mqtt_client.publish(MQTT_TOPIC, command)
            print(f"[MQTT] 已發送指令 '{command}' 到 topic '{MQTT_TOPIC}'")
        elif command == "NONE":
            print("[系統] 不需要任何操作")
        else:
            print(f"[警告] AI 回覆了非預期內容: '{command}'，已跳過")

    # 結束 MQTT 連線
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("[MQTT] 已斷線")


if __name__ == "__main__":
    main()
