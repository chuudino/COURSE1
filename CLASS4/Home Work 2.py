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
