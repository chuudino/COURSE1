# print("hello " + "Dino " * 3)  # practise add function with string
# print(max(1, 2, 3, 4, 5))  # practise max function
# print(len("hello"))  # practise len function
# print(type(True))  # practise type function
# print(type(123))
# print(type(123.456))
# print(type("hello"))
# print(int(True))  # practise int function
# print(int("123"))
# print(int("Hello")) # can't convert string to int
# print(float(True))  # practise float function
# print(float("123"))
# print(float("Hello")) # can't convert string to float
# print(str(True))  # practise str function
# print(str(123))
# print(str(123.456))
# print(bool(123.456))  # practise bool function
# print(bool("Hello"))
# print(bool(""))
# print(bool(0))
# print(bool(-1))
# print("開始輸入")
# input()
# print("輸入結果")
# print("可以把輸入的東西存起來")
# a = input()  # 可以用input()取出輸入的東西
# print("輸入的內容")
# print(a)
# print("透過input輸入的資料型態為")
# print(type(a))
# a = input("這是提示使用者輸入的文字,請輸入")
# print(a)

# a = float(input("請輸入半徑"))
# area = 3.14 * a**2
# print("半徑為", a, "公尺,面積為", area, "平方公尺")
# print("半徑為" + str(a) + "公尺,面積為" + str(area) + "平方公尺")
# print(f"半徑為{a}公尺,面積為{area}平方公尺")
# try: # 嘗試可能會有錯誤的程式
#     num = int(input("請輸入一個數字"))
# except: # 當有錯誤時要執行的程式
#     print("請輸錯誤")
# else: # 當沒有錯誤時要執行的程式
#     total = num + 1
#     print(total)
# finally: # 當try結束時要執行的程式
#     print("try 結束")

# print("程式繼續執行")
print(1 == 1)  # 等於
print(1 != 1)  # 不等於
print(1 < 1)  # 小於
print(1 > 1)  # 大於
print(1 <= 1)  # 小於等於
print(1 >= 1)  # 大於等於
print(1 == 1 and 1 == 1)  # 等於且, and專門處裡bool型態, 全部為True就會返回True
print(1 == 1 or 1 == 1)  # 等於或, or專門處裡bool型態, 其中一個為True就會返回True
print(not 1 == 1)  # not專門處裡bool型態, 與原本bool值的相反
