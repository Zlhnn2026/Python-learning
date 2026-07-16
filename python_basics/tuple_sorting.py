# ==============================
# Tuple Sorting Learning Notes
# ==============================

# 1. 字典数据
c = {'a': 10, 'b': 1, 'c': 22}

print("原始字典:", c)

# ==============================
# 方法1：手动转换 (value, key)
# ==============================

lst = []

for k, v in c.items():
    lst.append((v, k))   # 交换 key 和 value

print("转换后的列表:", lst)

# 排序（按 value）
lst = sorted(lst, reverse=True)

print("排序后结果:", lst)

# 输出 top
print("\nTop results:")
for val, key in lst:
    print(key, val)

# ==============================
# 方法2：一行写法（进阶）
# ==============================

print("\n一行写法结果:")
print(sorted([(v, k) for k, v in c.items()], reverse=True))

# ==============================
# 方法3：按 value 排序（推荐写法）
# ==============================

print("\nlambda写法:")

print(sorted(c.items(), key=lambda x: x[1], reverse=True))