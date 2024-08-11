# '''
# 當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
# EX:
# 請輸入0~100的整數:50
# 再小一點
# 請輸入0~50的整數:25
# 再小一點
# 請輸入0~25的整數:15
# 再大一點
# 請輸入15~25的整數:30
# 再小一點
# 請輸入15~25的整數:10
# 再大一點
# 請輸入15~25的整數:20
# 再大一點
# 請輸入20~25的整數:23
# 再大一點
# 請輸入23~25的整數:24
# 恭喜猜中!
# '''
# import random

# Answer = random.randint(1, 100)
# Result_Bottom = int(0)
# Result_Top = int(100)
# Result = int(input(f"請輸入{Result_Bottom}~{Result_Top}的整數: "))
# while True:
#     if Result == Answer:
#         print("恭喜猜中了！")
#         break
#     elif Result > Answer:
#         Result_Top = Result
#         print("再小一點")
#         Result = int(input(f"請輸入{Result_Top}~{Result_Bottom}的整數: "))
#     elif Result < Answer:
#         Result_Bottom = Result
#         print("再大一點")
#         Result = int(input(f"請輸入{Result_Bottom}~{Result_Top}的整數: "))
import random

Answer = random.randint(1, 100)  # 產生1~100的隨機整數
Result_Bottom = 1  # 設定猜數字的範圍
Result_Top = 100  # 設定猜數字的範圍
while True:  # 重複執行直到猜中
    try:  # 錯誤處理，如果輸入的不是數字，就會跳到except
        Result = int(input(f"請輸入{Result_Bottom}~{Result_Top}的整數:"))
    except:  # 輸入的不是數字, 跳到這裡
        print("請輸入數字")
        continue  # 跳回while開始的地方
    if Result == Answer:  # 猜中了
        print("恭喜猜中了！")
        break  # 跳出while迴圈, 結束程式
    elif Result > Answer:  # 猜的數字比答案大
        if Result < Result_Top:  # 如果猜的數字比上次猜的數字小
            Result_Top = Result  # 更新猜數字的範圍
        print("再小一點")
    elif Result < Answer:  # 猜的數字比答案小
        if Result > Result_Bottom:  # 如果猜的數字比上次猜的數字大
            Result_Bottom = Result  # 更新猜數字的範圍
        print("再大一點")
