"""
YouTube 音頻下載裁切工具
- 從 YouTube 下載音頻
- 設定頭尾裁切時間
- 輸出為 MP3 格式
"""

import os
import re
import tempfile
import yt_dlp
from pydub import AudioSegment


def sanitize_filename(filename: str) -> str:
    """清理檔名，移除非法字元"""
    # 移除 Windows 非法字元
    illegal_chars = r'[<>:"/\\|?*]'
    clean_name = re.sub(illegal_chars, "", filename)
    # 移除前後空白
    clean_name = clean_name.strip()
    # 限制長度
    if len(clean_name) > 200:
        clean_name = clean_name[:200]
    return clean_name if clean_name else "output"


def parse_time(time_str: str) -> int:
    """
    將時間字串轉換為毫秒
    支援格式: SS, MM:SS, HH:MM:SS
    """
    if not time_str or time_str.strip() == "":
        return 0

    parts = time_str.strip().split(":")
    try:
        if len(parts) == 1:
            # 只有秒數
            return int(float(parts[0]) * 1000)
        elif len(parts) == 2:
            # MM:SS
            minutes = int(parts[0])
            seconds = float(parts[1])
            return int((minutes * 60 + seconds) * 1000)
        elif len(parts) == 3:
            # HH:MM:SS
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = float(parts[2])
            return int((hours * 3600 + minutes * 60 + seconds) * 1000)
        else:
            raise ValueError("時間格式錯誤")
    except ValueError as e:
        print(f"時間格式錯誤: {time_str}")
        raise e


def format_duration(ms: int) -> str:
    """將毫秒轉換為可讀時間格式"""
    total_seconds = ms // 1000
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"


def get_video_info(url: str) -> dict:
    """取得 YouTube 影片資訊"""
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title", "Unknown"),
            "duration": info.get("duration", 0),  # 秒
            "duration_ms": info.get("duration", 0) * 1000,  # 毫秒
        }


def download_audio(url: str, output_path: str) -> str:
    """
    從 YouTube 下載音頻
    回傳下載的檔案路徑
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": output_path,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # yt-dlp 會自動加上 .mp3 副檔名
    mp3_path = output_path + ".mp3"
    if os.path.exists(mp3_path):
        return mp3_path
    # 如果路徑已經包含 .mp3
    if os.path.exists(output_path):
        return output_path

    raise FileNotFoundError(f"下載的檔案找不到: {output_path}")


def trim_audio(input_file: str, start_ms: int, end_ms: int, output_file: str) -> str:
    """
    裁切音頻檔案
    start_ms: 開始時間（毫秒）
    end_ms: 結束時間（毫秒），0 表示到結尾
    """
    print(f"載入音頻檔案: {input_file}")
    audio = AudioSegment.from_mp3(input_file)

    total_duration = len(audio)
    print(f"音頻總長度: {format_duration(total_duration)}")

    # 如果 end_ms 為 0 或超過總長度，設為總長度
    if end_ms <= 0 or end_ms > total_duration:
        end_ms = total_duration

    # 確保 start_ms 合理
    if start_ms < 0:
        start_ms = 0
    if start_ms >= end_ms:
        raise ValueError("開始時間必須小於結束時間")

    print(f"裁切範圍: {format_duration(start_ms)} ~ {format_duration(end_ms)}")

    # 裁切
    trimmed = audio[start_ms:end_ms]

    # 確保輸出路徑有 .mp3 副檔名
    if not output_file.lower().endswith(".mp3"):
        output_file += ".mp3"

    # 輸出
    print(f"輸出檔案: {output_file}")
    trimmed.export(output_file, format="mp3", bitrate="192k")

    print(f"完成! 輸出長度: {format_duration(len(trimmed))}")
    return output_file


def main():
    """主程式 - CLI 互動流程"""
    print("=" * 50)
    print("  YouTube 音頻下載裁切工具")
    print("=" * 50)
    print()

    # 1. 輸入 YouTube URL
    url = input("請輸入 YouTube 網址: ").strip()
    if not url:
        print("錯誤: 請輸入有效的網址")
        return

    # 2. 取得影片資訊
    print("\n正在取得影片資訊...")
    try:
        info = get_video_info(url)
    except Exception as e:
        print(f"錯誤: 無法取得影片資訊 - {e}")
        return

    video_title = info["title"]
    duration_ms = info["duration_ms"]

    print(f"\n影片標題: {video_title}")
    print(f"影片長度: {format_duration(duration_ms)}")

    # 3. 輸入檔名（預設使用影片標題）
    default_filename = sanitize_filename(video_title)
    filename_input = input(
        f"\n輸出檔名 (按 Enter 使用預設: {default_filename}): "
    ).strip()

    if filename_input:
        output_filename = sanitize_filename(filename_input)
    else:
        output_filename = default_filename

    # 4. 輸入開始時間
    start_input = input(
        "\n開始時間 (格式 MM:SS 或 HH:MM:SS，按 Enter 從頭開始): "
    ).strip()
    try:
        start_ms = parse_time(start_input) if start_input else 0
    except ValueError:
        print("錯誤: 開始時間格式不正確")
        return

    # 5. 輸入結束時間
    end_input = input(f"結束時間 (格式 MM:SS 或 HH:MM:SS，按 Enter 到結尾): ").strip()
    try:
        end_ms = parse_time(end_input) if end_input else duration_ms
    except ValueError:
        print("錯誤: 結束時間格式不正確")
        return

    # 驗證時間
    if start_ms >= end_ms:
        print("錯誤: 開始時間必須小於結束時間")
        return

    print(f"\n裁切範圍: {format_duration(start_ms)} ~ {format_duration(end_ms)}")

    # 6. 設定輸出路徑（與 mp3.py 同目錄）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, output_filename)

    # 7. 下載音頻到暫存
    print("\n正在下載音頻...")
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "temp_audio")
            downloaded_file = download_audio(url, temp_file)

            # 8. 裁切並輸出
            print("\n正在裁切音頻...")
            final_output = trim_audio(downloaded_file, start_ms, end_ms, output_path)

            print("\n" + "=" * 50)
            print(f"  完成！檔案已儲存至:")
            print(f"  {final_output}")
            print("=" * 50)

    except Exception as e:
        print(f"\n錯誤: {e}")
        return


if __name__ == "__main__":
    main()
