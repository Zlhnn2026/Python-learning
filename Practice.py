name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    print("①原始行:", line)
    if line.startswith("From "):
        words = line.split()
        print("②split结果:", words)
        email = words[1]
        print("③提取email:", email)
        counts[email] = counts.get(email, 0) + 1
        print("④当前统计:", counts)
        print("----------------------")
print("\n最终字典:", counts)
# 找最大值
big_email = None
big_count = None
for email, count in counts.items():
    print("⑤遍历:", email, count)
    if big_count is None or count > big_count:
        big_email = email
        big_count = count
print("\n最大值结果:")
print(big_email, big_count)

fhand = open('remeo.txt')  # 打开文件
counts = {}  # 创建空白字典
for line in fhand:
    words = line.split()  # 空白符作为分隔符对fhand分割
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # 计算每个word出现的次数

lst = []  # 创建空白列表
for key, val in counts.items():  # 将counts转换成元组列表
    newtup = (val, key)  # 将键值进行翻转,按值排序
    lst.append(newtup)  # 将元组元素读取到lst列表中
lst = sorted(lst, reverse=True)  # 降序
for val, key in lst[:10]:
    print(key, val)
list(map(lambda x, y: str(x)+'_'+y, range(5), list('abcde')))
