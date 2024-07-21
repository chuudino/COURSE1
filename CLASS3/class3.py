# password = input("請輸入密碼:")
# if password == "123456":  # 如果密碼為123456
#     print("密碼正確")
# elif password == "234567":  # 如果密碼為234567
#     print("歡迎加入")
# else:  # 如果上述密碼都不符合
#     print("密碼錯誤")

# SCORE = int(input("請輸入分數:"))
# if SCORE >= 90:  # 如果分數為90及以上
#     print("A")
# elif SCORE >= 80:  # 如果分數為80及以上
#     print("B")
# elif SCORE >= 70:  # 如果分數為70及以上
#     print("C")
# elif SCORE >= 60:  # 如果分數為60及以上
#     print("D")
# else:  # 如果分數為低於60
#     print("E")
import turtle as t  # 引入turtle模組 並命名為t

# t.forward(100)  # 前進100pixels
# t.right(90)  # 向左轉90度
# t.forward(100)  # 前進100pixels
# t.right(90)  # 向右轉90度
# t.forward(100)  # 前進100pixels
# t.right(90)  # 向左轉90度
# t.forward(100)  # 前進100pixels
# t.done()  # 結束turtle 一定要放在最後一行 如此視窗才不會自動關閉

# for i in range(5):  # i is a variable that takes on the values 0, 1, 2, 3, and 4
#     print(i)  # 輸出0,1,2,3,4
# for i in range(2, 5):  # i is a variable that takes on the values 2, 3, and 4
#     print(i)  # 輸出2,3,4
# for i in range(2, 10, 2):  # i is a variable that takes on the values 2, 4, 6, 8
#     print(i)  # 輸出2,4,6,8


# for i in range(4):
#     t.forward(100)  # 前進100pixels
#     t.right(90)  # 向右轉90度
# t.done()  # 結束turtle 一定要放在最後一行 如此視窗才不會自動關閉

# t.color("blue")  # 設定顏色為藍色
# t.shape("turtle")  # 設定形狀為turtle
# t.penup()  # 將筆頭向上移動

# for step in range(5, 128, 2):
#     t.stamp()  # 將筆頭移動到形狀的中心
#     t.forward(step)  # 前進step pixels
#     t.right(35)  # 向右轉25度

# t.done()  # 結束turtle 一定要放在最後一行 如此視窗才不會自動關閉

# x = int(input("請輸入x:"))  # 定義x為輸入的x
# sum = 0  # 定義sum為0
# for i in range(x + 1):  # i從0開始，直到x+1為止
#     sum += i  # 將i加到sum上, +=代表累加
# print(sum)  # 輸出結果為sum

# 99乘法表
# for i in range(1, 10):  # i從1開始，直到9為止
#     for j in range(1, 10):  # j從1開始，直到9為止
#         print(f"{i} * {j} = {i * j}")  # 輸出i*j的結果

# a = 100
# a += 2  # a=a+2, 相當於把a更新為a+2
# print(a)
# a -= 2  # a=a-2, 相當於把a更新為a-2
# print(a)
# a *= 2  # a=a*2, 相當於把a更新為a*2
# print(a)
# a /= 2  # a=a/2, 相當於把a更新為a/2
# print(a)
# a //= 2  # a=a//2, 相當於把a更新為a//2
# print(a)
# a %= 2  # a=a%2, 相當於把a更新為a%2
# print(a)
# a **= 2  # a=a**2, 相當於把a更新為a**2
# print(a)

# i = 0
# while i < 10:  # i=0, 直到i為9為止
#     print(i)  # 輸出i
#     i += 1  # i=i+1, 相當於把i更新為i+1

# password = ""
# while password != "123456":
#     password = input("請輸入密碼:")
#     if password == "123456":  # 如果密碼為123456
#         print("密碼正確")
#     else:  # 如果上述密碼都不符合
#         print("密碼錯誤")


# password = ""
# while password != "123456" and password != "234567":
#     password = input("請輸入密碼:")
#     if password == "123456":  # 如果密碼為123456
#         print("密碼正確")
#     elif password == "234567":  # 如果密碼為234567
#         print("歡迎加入")
#     else:  # 如果上述密碼都不符合
#         print("密碼錯誤")

while True:  # 循環
    password = input("請輸入密碼:")
    if password == "123456":  # 如果密碼為123456
        print("密碼正確")
        break  # 退出循環
    elif password == "234567":  # 如果密碼為234567
        print("歡迎加入")
        break  # 退出循環
    else:  # 如果上述密碼都不符合
        print("密碼錯誤")
