book = {
    "書名": "海邊的卡夫卡",
    "作者": "小松",
    "出版社": "月曜日社",
    "類型": "科幻",
    "描述": "一個女孩在海裡的海滅之後，她們的生活只剩下一個相同的卡夫卡，但是卡夫卡的意義變成了她們的生活。",
}  # 建立字典
print(book["作者"])  # 取出字典內的值
print(book["類型"])  # 取出字典內的值
book["類型"] = "歷史"  # 更改字典內的值
print(book["類型"])  # 取出字典內的值
book["頁數"] = 100  # 加入新的key-value
print(book["頁數"])  # 取出字典內的值


for key in book:  # 使用for迴圈逐字典的key印出內容
    print(f"{key}: {book[key]}")

for key in book.keys():  # 使用for迴圈逐字典的key印出內容
    print(f"{key}: {book[key]}")

for value in book.values():  # 使用for迴圈逐字典的value印出內容
    print(f"{value}")

for key, value in book.items():  # 使用for迴圈逐字典的key和value印出內容
    print(f"{key}: {value}")


# in 在list中查找是否存在某個元素
book2 = ["書名", "作者", "出版社", "類型", "描述"]
if "書名" in book2:  # 判斷是否存在某個key
    print("存在")

# in 在字典中查找是否存在某個key
"""
book = {
    "書名": "海邊的卡夫卡",
    "作者": "小松",
    "出版社": "月曜日社",
    "類型": "歷史",
    "描述": "一個女孩在海裡的海滅之後，她們的生活只剩下一個相同的卡夫卡，但是卡夫卡的意義變成了她們的生活。",
}  # 建立字典
"""
if "書名" in book:  # 判斷是否存在某個key
    print("存在")
if "歷史" in book:  # 判斷是否存在某個key
    print("歷史有在字典裡面")

# print(book.values())
if "歷史" in book.values():  # 判斷是否存在某個key
    print("歷史有在字典裡面")

# pop 刪除字典內的key-value
if "描述" in book:  # 判斷是否存在某個key
    book.pop("描述")  # 刪除字典內的key-value
    print(book)
