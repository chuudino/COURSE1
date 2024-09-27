# """
# 題目：餐點點餐系統

# 請根據以下需求，完成一個簡單的餐點點餐系統。該系統應該能夠讓使用者新增餐點、移除餐點以及提交菜單。

# 功能需求：

# 1. 顯示目前已點的餐點
#    - 每次迴圈開始時，顯示目前已點的餐點列表。

# 2. 新增餐點
#    - 提供選項讓使用者新增餐點。
#    - 顯示所有可選擇的果汁。
#    - 使用者輸入餐點編號後，將對應的果汁新增到已點餐點列表中。
#    - 若輸入非數字或超出範圍的編號，提示錯誤訊息並要求重新輸入。

# 3. 移除餐點
#    - 提供選項讓使用者移除已點的餐點。
#    - 使用者輸入想移除的餐點名稱，從已點餐點列表中移除該餐點。
#    - 若輸入的餐點名稱在已點餐點列表中出現多次，則移除所有該名稱的餐點。

# 4. 提交菜單
#    - 提供選項讓使用者提交菜單。
#    - 顯示已點的所有餐點及其數量。
#    - 結束程式。

# 5. 錯誤處理
#    - 若使用者輸入無效的功能選項，提示錯誤訊息並要求重新輸入。
# """
# 目前已點的餐: []
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:1
# ==========================
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:1
# 您點的商品是: 蘋果汁
# ==========================
# 目前已點的餐: ['蘋果汁']
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:1
# ==========================
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:2
# 您點的商品是: 柳橙汁
# ==========================
# 目前已點的餐: ['蘋果汁', '柳橙汁']
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:1
# ==========================
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:3
# 您點的商品是: 葡萄汁
# ==========================
# 目前已點的餐: ['蘋果汁', '柳橙汁', '葡萄汁']
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:1
# ==========================
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:1
# 您點的商品是: 蘋果汁
# ==========================
# 目前已點的餐: ['蘋果汁', '柳橙汁', '葡萄汁', '蘋果汁']
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:3
# ==========================
# 您點的餐點為
# 蘋果汁: 2
# 柳橙汁: 1
# 葡萄汁: 1
# 菜單已提交囉!
# E:\
# 目前已點的餐: []
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:sadassdasda
# ==========================
# 查無此功能請重新輸入!
# ==========================
# 目前已點的餐: []
# 1. 新增餐點
# 2. 移除餐點
# 3. 提交菜單
# 請輸入功能選項:1
# ==========================
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:5
# 輸入錯誤查無此餐點，請重新輸入餐點編號
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:ggg
# 請輸入數字編號
# 1. 蘋果汁
# 2. 柳橙汁
# 3. 葡萄汁
# 請輸入餐點編號:

Function_list = ["新增餐點", "移除餐點", "提交菜單"]
Menu_list = ["蘋果汁", "柳橙汁", "葡萄汁"]
# Oder_amount = [0, 0, 0]  # 定義餐點數量
Oder_amount = [0] * len(Menu_list)
while True:  # 讓程式無限循環直到使用者選擇退出
    for i in range(len(Function_list)):  # 用for迴圈印出功能清單
        print(f"{i+1}. {Function_list [i]}")  # i+1是為了讓清單從1開始
    try:  # 使用try來檢查使用者輸入的是否為數字
        choose_i = int(input("請輸入功能選項:")) - 1
         # 讓使用者輸入選擇的號碼後-1是為了取得正確的index
    except:  # 如果使用者輸入的不是數字就印出錯誤訊息
        print("查無此功能請重新輸入")
    continue
    if choose_i == 0:
        while True:
            for j in range(len(Menu_list)):  # 用for迴圈印出餐點清單
                   print(f"{j+1}. {Menu_list[j]}")
            try:
                choose_j = int(input("請輸入餐點編號:")) - 1
                if choose_j < len(Menu_list) and choose_j >= 0:
                    print(f"您點的餐點是: {Menu_list[choose_j]}")
                    Oder_amount[choose_j] = Oder_amount[choose_j] + 1
                    print(f"目前已點的餐點數量是{Oder_amount[choose_j]}")
            except:
                print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                continue
            break
    if choose_i == 1:
        try:
           choose_d = int(input("請輸入要移除的餐點編號:")) - 1
           if choose_d < len(Menu_list) and choose_d >= 0:
              Oder_amount[choose_d] = Oder_amount[choose_d] - 1
           if Oder_amount[choose_d] < 0:
                Oder_amount[choose_d] = 0
            print(f"移除後餐點數量是{Oder_amount[choose_d]}")
            print(f"選擇的餐點己移除")
        except:
            print("輸入錯誤查無此餐點，請重新輸入餐點編號")
        continue
    elif choose_i == 2:
        print("您點的餐點為:")
        Item = int(1)
        for k in range(len(Menu_list) - 1):
            if Oder_amount[k] == 0:
                continue
            else:
                print(f"{Item}   {k+1}.{Menu_list[k]} {: 數量} {Oder_amount[k]}")
                Item = Item + 1
        print("您點的餐點己提交.")
        for i in range(len(Oder_amount)):
            Oder_amount[i] = 0


####參考答案
Function_list = ["新增餐點", "移除餐點", "提交菜單"]  # 功能清單
Menu_list = ["蘋果汁", "柳橙汁", "葡萄汁"]  # 餐點清單
Oder_amount = []  # 訂單清單
while True:  # 讓程式無限循環直到使用者選擇退出
    for i in range(len(Function_list)):  # 用for迴圈印出功能清單
        print(f"{i+1}. {Function_list [i]}")  # i+1是為了讓清單從1開始
    try:  # 使用try來檢查使用者輸入的是否為數字
        choose_i = int(input("請輸入功能選項:")) - 1
        # 讓使用者輸入選擇的號碼後-1是為了取得正確的index
    except:  # 如果使用者輸入的不是數字就印出錯誤訊息
        print("查無此功能請重新輸入")
        continue  # 如果使用者輸入的不是數字就繼續循環
    if choose_i == 0:
        for j in range(len(Menu_list)):  # 用for迴圈印出餐點清單
            print(f"{j+1}. {Menu_list[j]}")
        while True:  # 讓程式無限循環直到使用者選擇退出
            try:
                choose_j = int(input("請輸入餐點編號:")) - 1
                if choose_j <= len(Menu_list) and choose_j >= 0:
                    print(f"您點的餐點是: {Menu_list[choose_j]}")
                    Oder_amount.append(Menu_list[choose_j])
                    print(f"目前已點的餐點數量是{Oder_amount[choose_j]}")
            except:
                print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                if input("是否繼續點餐(Y/N):").upper() == "Y":
                    # 使用者可以選擇是否繼續點餐
                    continue
                else:
                    break
            break  # 有完成點餐就跳出迴圈，繼續執行下一個功能

    if choose_i == 1:
        while True:
            try:
                choose_d = input("請輸入要移除的餐點名稱:")
                if choose_d in Oder_amount:
                    Oder_amount.remove(choose_d)
                    # list.remove(資料名稱)可以移除資料
                    # list.pop(資料標籤)也可以移除資料，但是要指定index
                print(f"移除後餐點數量是{Oder_amount}")
                print(f"選擇的餐點己移除")
            except:
                print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                if input("是否繼續點餐(Y/N):").upper() == "Y":
                    # 使用者可以選擇是否繼續點餐
                    continue
                else:
                    break
            break  # 有完成點餐就跳出迴圈，繼續執行下一個功能
    elif choose_i == 2:
        print("您點的餐點及數量為:")
        for i in Menu_list:  # 用for迴圈印出餐點清單，範圍是餐點清單
            print(
                f"{i} 有 {Oder_amount.count(i)} 個"
            )  # 使用.count()來計算清單中有幾個相同的資料
        print("您點的餐點己提交.")
        Oder_amount = []  # 提交菜單後清空訂單

####參考答案
Function_list = ["新增餐點", "移除餐點", "提交菜單"]  # 功能清單
Menu_list = ["蘋果汁", "柳橙汁", "葡萄汁"]  # 餐點清單
Oder_amount = []  # 訂單清單
while True:  # 讓程式無限循環直到使用者選擇退出
    for i in range(len(Function_list)):  # 用for迴圈印出功能清單
        print(f"{i+1}. {Function_list [i]}")  # i+1是為了讓清單從1開始
    try:  # 使用try來檢查使用者輸入的是否為數字
        choose_i = int(input("請輸入功能選項:")) - 1
        # 讓使用者輸入選擇的號碼後-1是為了取得正確的index
    except:  # 如果使用者輸入的不是數字就印出錯誤訊息
        print("查無此功能請重新輸入")
        continue  # 如果使用者輸入的不是數字就繼續循環
    if choose_i == 0:
        for j in range(len(Menu_list)):  # 用for迴圈印出餐點清單
            print(f"{j+1}. {Menu_list[j]}")
        while True:  # 讓程式無限循環直到使用者選擇退出
            try:
                choose_j = int(input("請輸入餐點編號:")) - 1
                if choose_j < len(Menu_list) and choose_j >= 0:
                    print(f"您點的餐點是: {Menu_list[choose_j]}")
                    Oder_amount.append(Menu_list[choose_j])
                    print(f"目前已點的餐點是{Oder_amount}")
            except:
                print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                if input("是否繼續點餐(Y/N):").upper() == "Y":
                    # 使用者可以選擇是否繼續點餐
                    continue
                else:
                    break
            break  # 有完成點餐就跳出迴圈，繼續執行下一個功能

    if choose_i == 1:
        while True:
            try:
                choose_d = input("請輸入要移除的餐點名稱:")
                if choose_d in Oder_amount:
                    Oder_amount.remove(choose_d)
                    # list.remove(資料名稱)可以移除資料
                    # list.pop(資料標籤)也可以移除資料，但是要指定index
                print(f"移除後餐點數量是{Oder_amount}")
                print(f"選擇的餐點己移除")
            except:
                print("輸入錯誤查無此餐點，請重新輸入餐點編號")
                if input("是否繼續點餐(Y/N):").upper() == "Y":
                    # 使用者可以選擇是否繼續點餐
                    continue
                else:
                    break
            break  # 有完成點餐就跳出迴圈，繼續執行下一個功能
    elif choose_i == 2:
        print("您點的餐點及數量為:")
        for i in Menu_list:  # 用for迴圈印出餐點清單，範圍是餐點清單
            print(
                f"{i} 有 {Oder_amount.count(i)} 個"
            )  # 使用.count()來計算清單中有幾個相同的資料
        print("您點的餐點己提交.")
        Oder_amount = []  # 提交菜單後清空訂單
