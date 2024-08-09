# jump = int(input("請輸入要跳繩的次數:"))
# for i in range(1, jump + 1):  # i=1, 直到jump為止
#     if i % 10 == 0:  # 如果i為0
#         print("休息一下吧")
#         continue  # 迴圈繼續回合
#     print(f"第{i}次跳繩")
# for i in range(2, 5):  # i=2, 直到4為止
#     print(f"第{i}")  # 輸出i
# else:  # 當break的情況不會執行, 但continue可以
#     print("迴圈正常結束")

import random

# # randrange設定方式跟range一樣
# print(random.randrange(1, 101))
# print(random.randrange(1, 101, 2))
# print(random.randrange(101))

# # randint必須設定開始數和結束數，抽籤範圍包含結束
# print(random.randint(1, 101))
# print(random.randint(5, 101))


# Answer = random.randint(1, 100)
# while True:  # 循環
#     Result = int(input("請輸入你猜的數字:"))
#     if Result == Answer:  # 如果猜對
#         print("恭喜你，猜對了！")
#         break  # 跳出循環
#     elif Result > Answer:  # 如果猜錯了
#         print("你猜錯了再小一點吧！")
#     else:  # 如果猜錯了
#         print("你猜錯了再大一點吧！")
# L = [1, 2, 3]
# print(L)
# L1 = [1, 2, 3, "Hello", "World"]
# print(L1)
# L2 = [1, 2, 3, "Hello", "World", [4, 5, 6]]
# print(L2)
# print(L2[0])
# print(L2[1])
# print(L2[2])
# print(L2[3])
# print(L2[4])
# print(L2[5])
# print(L2[5][0])
# print(L2[5][1])
# print(L2[5][2])


# L1 = [1, 2, 3, "Hello", "World", [1, 2, 3]]
# print(L1)
# print(L1[0])
# print(L1[1])
# print(L1[2])
# print(L1[3])
# print(L1[4])
# print(L1[5])
# print(L1[5][0])

# L0 = [0, 1, 2, 3, 4, 5, 6]
# print(L0[0:3])  # 取出0, 1, 2
# print(L0[3:6])  # 取出3, 4, 5
# print(L0[3:])  # 取出3, 4, 5, 6
# print(L0[:3])  # 取出0, 1, 2
# print(L0[:])  # 取出0, 1, 2, 3, 4, 5, 6
# print(L0[0:5:2])  # 取出0, 2, 4
# print(L0[::3])  # 取出0, 3, 6
# L0 = ["a", "b", "c"]
# for index in range(len(L0)):  # 循環
#     print(f"第{index}個元素的值為{L0[index]}")
# L0 = ["a", "b", "c"]
# for element in L0:  # List也可以當作迴圈變數的範圍
#     print(element)
