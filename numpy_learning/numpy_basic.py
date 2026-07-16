"""
NumPy基础

内容：
1. ndarray数组构造
2. 等差序列生成
3. 特殊矩阵
4. 随机数生成
5. 随机种子

学习来源：
Datawhale Joyful-Pandas
"""
#array 构造
import numpy as np
np.array([1,2,3])

#等差序列
np.linspace(1,5,11) # 起始、终止（包含）、样本个数
np.arange(1,5,2) # 起始、终止（不包含）、步长

#特殊矩阵 zeros, eye, full
np.zeros((2,3)) # 传入元组表示各维度大小 (排，列）
np.eye(3) # 3*3的单位矩阵
np.eye(3, k=1) # 偏移主对角线1个单位的伪单位矩阵
np.full((2,3), 10) # 元组传入大小，10表示填充数值
np.full((2,3), [1,2,3]) # 每行填入相同的列表

# 随机矩阵：np.random
# 最常用的随机生成函数为rand, randn, randint, choice，它们分别表示0-1均匀分布的随机数组、标准正态的随机数组、随机整数组和随机列表抽样：
np.random.rand(3) # 生成服从0-1均匀分布的三个随机数
np.random.random((2,3))
np.random.rand(3, 3) # 注意这里传入的不是元组，每个维度大小分开输入
'''
a, b = 5, 15
(b - a) * np.random.rand(3) + a
'''
#一般的，可以选择已有的库函数
np.random.uniform(5, 15, 3)
np.random.randn(3) #标准正态分布 N(0,1)
np.random.randn(2, 2) #正态分布2*2矩阵

# 对于由标准正态分布N(0,1)变成服从方差为σ^2均值为μ的一元正态分布可以如下生成：
sigma, mu = 2.5, 3
mu + np.random.randn(3) * sigma
# 利用标准正态分布 N(0,1)
# 转换为均值mu，标准差sigma的正态分布
# X = μ + σZ

# 可选择从已有函数生成：
np.random.normal(3, 2.5, 3)
# randint可以指定生成随机整数的最小值最大值（不包含）和维度大小：
low, high, size = 5, 15, (2,2) # 生成5到14的随机整数
np.random.randint(low, high, size)

# choice可以从给定的列表中，以一定概率和方式抽取结果，当不指定概率时为均匀采样，默认抽取方式为有放回抽样：
my_list = ['a', 'b', 'c', 'd']
np.random.choice(my_list, 2, replace=False, p=[0.1, 0.7, 0.1 ,0.1])#2：抽两个；replace=False：不放回抽样；p：各自概率，总和要等于1

np.random.choice(my_list, (3,3))#随机放回取样，3*3
# 当返回的元素个数与原列表相同时，不放回抽样等价于使用permutation，相当于打散原列表：
np.random.permutation(my_list)
np.random.shuffle(my_list)#随机打乱一个数组（或列表）的顺序

# 随机种子，它能够固定随机数的输出结果：
np.random.seed(0)# 0到1的均匀分布，固定随机种子，使随机结果可以复现
np.random.rand()#把随机数生成器固定在编号0的位置，生成0-1均匀分布随机数

# =========================
# 练习
# =========================

# 1. 创建一个3×3全为5的矩阵
#答案
import numpy as np
arr = np.full((3,3), 5)
print(arr)

# 2. 生成10个0-100之间随机整数
low, high, size = 0, 100, 10
arr = np.random.randint(low, high, size)
print(arr)

# 3. 固定随机种子，比较两次随机结果
np.random.seed(0)
a = np.random.rand()
print(a)
np.random.seed(0)
b = np.random.rand()
print(b)