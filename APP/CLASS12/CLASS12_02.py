# import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import sys

############################設定工作目錄############################
os.chdir(sys.path[0])

font = FontProperties(fname="LXGWWenKaiTC-Regular.ttf", size=20)
# 折線圖
# listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# listy = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# fig, ax = plt.subplots()
# ax.plot(listx, listy)
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_title("曲線圖", fontproperties=font)
# plt.show()

# # 定義數據
# labels = ["A", "B", "C", "D", "E"]
# values = [23, 85, 72, 43, 52]

# # 繪製柱狀圖
# plt.bar(labels, values, color="royalblue")
# plt.xlabel("類別", fontproperties=font)
# plt.ylabel("數量", fontproperties=font)
# plt.grid(True)
# plt.title("簡單柱狀圖範例", fontproperties=font)
# plt.show()


# # 條碼數據，1 表示黑色條，0 表示白色條
# barcode_data = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]

# # 設定條的寬度和高度
# bar_width = 0.8
# bar_height = 10

# # 建立圖形
# fig, ax = plt.subplots()

# # 手動計數器
# i = 0
# for bit in barcode_data:
#     color = "black" if bit == 1 else "white"
#     ax.bar(i, bar_height, color=color, width=bar_width)
#     i += 1  # 手動增加計數器

# # 隱藏軸線和刻度
# ax.axis("off")

# # 顯示圖形
# plt.show()


# import qrcode

# # 定義要轉成 QR code 的字串
# data = "這是 QR code 的內容"
# # 生成 QR code 圖像
# img = qrcode.make(data)
# # 儲存圖像
# img.save("qrcode.png")


import qrcode

data = "這是 QR code 的內容"
qr = qrcode.QRCode(
    version=1,  # 版本 (1-40, 控制 QR code 尺寸)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 錯誤更正等級
    box_size=10,  # 每個方塊的像素大小
    border=4,  # 邊框寬度
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("custom_qrcode.png")
