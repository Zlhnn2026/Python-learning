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