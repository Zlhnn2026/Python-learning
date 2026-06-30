"""
Day 1: Python基础（Datawhale）
内容：
1. 列表推导式与条件赋值
2. 匿名函数 lambda
3. zip / enumerate
"""

# 1. 列表推导式
L = [x*2 for x in range(5)]
print(L)


# 2. lambda
f = lambda x: 2*x
print(f(3))


# 3. zip
a = ['a','b','c']
b = [1,2,3]
print(list(zip(a,b)))


# 4. enumerate
for i, v in enumerate(a):
    print(i, v)