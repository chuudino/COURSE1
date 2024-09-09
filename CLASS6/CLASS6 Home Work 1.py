# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:1
# ==========================
# 請輸入想新增的科目:en
# 請輸入分數:100
# ==========================
# en:100
# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:1
# ==========================
# 請輸入想新增的科目:ch
# 請輸入分數:aaaaa
# 輸入錯誤，請重新輸入
# 請輸入分數:2
# ==========================
# en:100
# ch:2
# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:1
# ==========================
# 請輸入想新增的科目:math
# 請輸入分數:55
# ==========================
# en:100
# ch:2
# math:55
# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:2
# ==========================
# 請輸入想刪除的科目:abc
# 此科目尚未新增!
# ==========================
# en:100
# ch:2
# math:55
# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:2
# ==========================
# 請輸入想刪除的科目:en
# 刪除成功!
# ==========================
# ch:2
# math:55
# 1. 新增科目成績
# 2. 刪除科目成績
# 3. 提交所有成績並顯示平均
# 請輸入功能編號:3
# ==========================
# ch:2
# math:55
# 總平均為:28.5

Function_list = ["新增科目成績", "刪除科目成績", "提交所有成績並顯示平均"]  # 功能清單
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

    if choose_i == 0:  # 新增科目成績
        while True:
            try:
                Course = str(input(f"請輸入想新增的科目:"))
                break
            except:
                print("請輸入正確的科目!")
                continue
        while True:  # 判斷是否存在某個key
            if Course in GradeBook_Dino.keys():  # 判斷是否存在某個key
                print("此科目已存在!")
                break
            try:
                Grade = int(input(f"請輸入分數:"))
            except:
                print("分數輸入錯誤，請重新輸入")
                continue
            if Grade > 100 or Grade < 0:
                print("分數輸入錯誤，請重新輸入")
                continue
            GradeBook_Dino.update({Course: Grade})
            print(f"您的成績已新增!")
            break

    elif choose_i == 1:
        Course = str(input(f"請輸入想刪除科目成績:"))
        if Course in GradeBook_Dino.keys():  # 判斷是否存在某個key
            V = GradeBook_Dino.pop(Course)
            print(f"{Course}: {V} 刪除成功!")
        else:
            print("此科目尚未新增!")

    elif choose_i == 2:
        if not GradeBook_Dino:
            print("目前您尚未新增任何成績!")
            continue
        else:
            Total = 0
            for key, value in GradeBook_Dino.items():
                print(f"{key}: {value}")
                Total = Total + int(value)
        print(f"總平均為:{Total / len(GradeBook_Dino)}")
    continue
