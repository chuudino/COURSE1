def hello():  # 定義函數，要用def開頭，後面接函數名稱，後面接括號:
    print("Hello, World!")  # 函數內容


hello()  # 呼叫函數


def add(x, y):  # 定義函數, x,y為傳入參數,他們是區域變數所以只能在函數內使用
    return x + y  # 回傳x+y的值


ans = add(3, 5)  # 呼叫函數
print(ans)  # 呼叫函數


def sub(x):  # 定義函數
    y = ans - x  # 可以使用全域變數來進行運算，但是不能更改全域變數的值
    return y


print(sub(2))  # 呼叫函數


def mul(x):  # 定義函數
    ans = x * 2  # 如果呼叫了與全域變數相同名稱的變數，則會是一個新的區域變數


mul(2)
print(ans)  # 呼叫函數


# 在指令範圍內更改全域變數
def change():
    global ans  # 宣告ans為全域變數,可以在函數內更改全域變數的值
    ans = 10  # 更改ans的值


def change2(x):
    x = 10
    # 比較安全更改全域變數的值, 就是將全域變數當作參數傳入函數, 並回傳更改後的值
    return x


ans = change2(ans)
print(ans)


def add(x: int, y: int) -> int:  # 新增傳入參數的型態提示和回傳值的型態提示
    """
    這是一個加法函數
    """
    # 上面是指令描述區，用"""來包住指令描述
    return x + y  # 回傳x+y的值


# 指令的預設值
def add(x: int, y: int, z: int = 100) -> int:  # 定義函數
    """
    參數:  \n
    x: int \n
    y: int \n
    z: int = 100 \n

    回傳:
    int

    這是一個加法函數
    """
    return x + y + z


print(add("1", "2", "3"))  # 可以強制傳入非整數的值, 指令內不僅供提示不會阻擋程式執行
# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    # length = length + 1 # 這行會出錯，
    # 因為在函數內部length是區域變數，不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯，因為area是區域變數，只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
# 因為要等到函數被呼叫時才會執行，所以area的值是在函數被呼叫時才會被計算


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100
# 這時候指令內部的area是區域變數，不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length是全域變數, area是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是 25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用global，將area變成全域變數，可以在函數內部修改全域變數的值
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 25


def hello(name: str):  # 函數傳入參數都是區域變數
    """
    指令說明區 \n
    這是一個打招呼的函數 \n
    參數:\n
    name: str - 姓名

    回傳:None

    範例:hello("Alice") # Hello, Alice!
    """
    print(f"Hello, {name}!")


def roll_dice(n: int) -> list[int]:
    """
    指令說明區\n
    這是一個擲骰子的函數\n
    參數:\n
    n: int - 擲骰子的次數

    回傳:list

    範例:roll_dice(3) # 3
    """
    import random as r

    result = []
    for i in range(n):
        result.append(r.randint(1, 6))
    return result


roll_history = roll_dice(300)
print(roll_history)
