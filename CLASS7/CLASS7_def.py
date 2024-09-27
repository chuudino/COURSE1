# Function_list = ["新增科目成績", "刪除科目成績", "提交所有成績並顯示平均"]  # 功能清單
# GradeBook_Dino = {}  # 建立空的字典
# items = GradeBook_Dino.items()  # 取出字典內的key

# while True:  # 讓程式無限循環直到使用者選擇退出
#     for key, value in GradeBook_Dino.items():
#         print(f"{key}: {value}")
#     for i in range(len(Function_list)):  # 用for迴圈印出功能清單
#         print(f"{i+1}. {Function_list [i]}")  # i+1是為了讓清單從1開始
#     try:  # 使用try來檢查使用者輸入的是否為數字
#         choose_i = int(input("請輸入功能選項:")) - 1
#         if choose_i < 0 or choose_i >= 3:
#             print("請輸入正確的功能選項!")
#     except:
#         print("請輸入正確的功能選項!")
#         continue

#     if choose_i == 0:  # 新增科目成績
#         Course = input(f"請輸入想新增的科目:")
#         while True:  # 判斷是否存在某個key
#             try:
#                 Grade = int(input(f"請輸入分數:"))
#             except:
#                 print("分數輸入錯誤，請重新輸入")
#                 continue
#             if Grade > 100 or Grade < 0:
#                 print("分數輸入錯誤，請重新輸入")
#                 continue
#             GradeBook_Dino[Course] = Grade
#             print(f"您的成績已新增!")
#             break

#     elif choose_i == 1:
#         Course = str(input(f"請輸入想刪除科目成績:"))
#         if Course in GradeBook_Dino.keys():  # 判斷是否存在某個key
#             V = GradeBook_Dino.pop(Course)  # 回傳值是分數
#             print(f"{Course}: {V} 刪除成功!")
#         else:
#             print("此科目尚未新增!")

#     elif choose_i == 2:
#         if not GradeBook_Dino:
#             print("目前您尚未新增任何成績!")
#         else:
#             print(f"總平均為:{sum(GradeBook_Dino.values()) / len(GradeBook_Dino)}")

####################################################################################################


def add_grade():
    # 新增科目成績
    Course = input(f"請輸入想新增的科目:")
    while True:  # 判斷是否存在某個key
        try:
            Grade = int(input(f"請輸入分數:"))
        except:
            print("分數輸入錯誤，請重新輸入")
            continue
        if Grade > 100 or Grade < 0:
            print("分數輸入錯誤，請重新輸入")
            continue
        GradeBook_Dino[Course] = Grade
        print(f"您的成績已新增!")
        break


def delete_grade():
    Course = str(input(f"請輸入想刪除科目成績:"))
    if Course in GradeBook_Dino.keys():  # 判斷是否存在某個key
        V = GradeBook_Dino.pop(Course)  # 回傳值是分數
        print(f"{Course}: {V} 刪除成功!")
    else:
        print("此科目尚未新增!")


def average():
    if not GradeBook_Dino:
        print("目前您尚未新增任何成績!")
    else:
        print(f"總平均為:{sum(GradeBook_Dino.values()) / len(GradeBook_Dino)}")


Function_list = ["新增科目成績", "刪除科目成績", "提交所有成績並顯示平均"]  # 功能清單
def_list = [add_grade, delete_grade, average]  # 功能函數清單
GradeBook_Dino = {}  # 建立空的字典
items = GradeBook_Dino.items()  # 取出字典內的key

while True:  # 讓程式無限循環直到使用者選擇退出
    for key, value in GradeBook_Dino.items():
        print(f"{key}: {value}")
    for i in range(len(Function_list)):  # 用for迴圈印出功能清單
        print(f"{i+1}. {Function_list [i]}")  # i+1是為了讓清單從1開始
    try:  # 使用try來檢查使用者輸入的是否為數字
        choose_i = int(input("請輸入功能選項:")) - 1
        if choose_i < 0 or choose_i >= 3:
            print("請輸入正確的功能選項!")
    except:
        print("請輸入正確的功能選項!")
        continue

    def_list[choose_i]()  # 使用者選擇的功能
