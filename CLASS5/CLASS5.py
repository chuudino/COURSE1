# a = [1, 2, 3]
# b = a #call by reference 共用同一内存
# b[0] = 2
# print(a)
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 2
# print(a)
# print(b)
# print(a + b)
# print(a * 10)
# print(max(a))
# print(min(b))
# print(list("abc"))
# print("1, 2, 3".split(","))
# print("2022/1/2".split("/"))
# img = ["1", "2", "3"]
# print("-".join(img))
# l = [1, 2, 3]
# l.append(4)
# print(l)
# l = ["a", "b", "c", "a"]
# l.remove("a")
# print(l)
# l.pop()
# print(l)
# l.pop(0)
# print(l)
# l.insert(0, "a")
# print(l)
# l = [9, 1, -4, 2, 3, 7, 11, 3]
# print(l.count(3))
# l.sort()
# print(l)
# l.sort(reverse=True)  # reverse=True可以將排序後的列表元素倒序
# print(l)
l = [9, 1, -4, 2, 3, 7, 11, 3]
# l.reverse()  # 與sort(reverse=True)不相同, reverse()只是將列表元素倒序
print(l)
print(l.index(3))
