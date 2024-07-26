# 畫出時鐘秒針
# turtle.home() # 回到中心點
# turtle.clear() # 清空畫面指令
# import time  # 匯入time模組
# time.sleep(1) # 延遲1秒

import turtle as t  # 引入turtle模組 並命名為t
import time as ti  # 匯入time模組

t.clear()  # 清空畫面指令
#
for i in range(0, 366, 6):
    # t.circle(120)  # 畫圓形100pixels
    t.home()  # 向左轉90度
    t.clear()  # 清空畫面指令
    t.left(90 - i)  # 向左轉90 - i  度
    t.pendown()  # 將筆頭向下移動
    t.forward(100)  # 前進100pixels
    t.penup()  # 將筆頭向上移動
    ti.sleep(1)  # 延遲1秒
t.done()  # 結束turtle 一定要放在最後一行 如此視窗才不會自動關閉
