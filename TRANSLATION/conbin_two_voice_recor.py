import ffmpeg

input1 = ffmpeg.input(r"D:\Python\TRANSLATION\audio1.m4a")
input2 = ffmpeg.input(r"D:\Python\TRANSLATION\audio2.m4a")

# 使用 concat 過濾器合併音檔
ffmpeg.concat(input1, input2, v=0, a=1).output(
    r"D:\Python\TRANSLATION\output.m4a"
).run()
