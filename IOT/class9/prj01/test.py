import mcu
import time

mp3 = mcu.MP3()
mp3.start(volume=100, song=1)  # 播放音樂
time.sleep(5)
mp3.stop()
