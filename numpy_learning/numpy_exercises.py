"""
Numpy 基础练习
来源：
Datawhale Numpy基础
学习目标：
1. 理解NumPy数组计算逻辑
2. 掌握循环思维向向量化思维转换
3. 理解广播机制
4. 学习矩阵运算优化
核心思想：
NumPy最大的优势不是写更少代码，
而是把循环转换成数组整体计算。
"""
import numpy as np
#=========================
'''
Ex1：利用列表推导式写矩阵乘法
一般的矩阵乘法根据公式，可以由三重循环写出，请将其改写为列表推导式的形式。

M1 = np.random.rand(2,3)
M2 = np.random.rand(3,4)
res = np.empty((M1.shape[0],M2.shape[1]))
for i in range(M1.shape[0]):
    for j in range(M2.shape[1]):
        item = 0
        for k in range(M1.shape[1]):
            item += M1[i][k] * M2[k][j]
        res[i][j] = item
(np.abs((M1@M2 - res) < 1e-15)).all() # 排除数值误差

理解：首先i,j循环过后，i,j有8种组合方式，然后item=0，k循环3种，然后累加item，ij从（0，0）开始，
一共有8个(i,j)组合,每一个(i,j)位置都有自己的item,item只负责计算当前res[i][j],8个位置之间不是相加关系
然后答案的三个循环写到一起，意思是先把k循环带入三个表达式然后相加，再带j就是12个表达式相加，再带i就是24个表达式相加
# 矩阵乘法过程：
# i决定结果矩阵的行
# j决定结果矩阵的列
# k表示当前元素计算时的中间累加维度
#
# 对于res[i][j]:
# 固定i和j后，通过k遍历：
# M1[i][0]*M2[0][j]
# M1[i][1]*M2[1][j]
# M1[i][2]*M2[2][j]
# 最后累加得到当前位置的结果
'''

# 解答
# 参考答案
# 使用列表推导式改写：
# 不是简单把三个循环压缩到一行
# 而是分层转换：
# 1. k循环：
#    一个结果元素 = 固定i,j后，对k方向进行累加
#    使用sum()代替item +=
# 2. j循环：
#    生成一行结果
# 3. i循环：
#    生成整个结果矩阵
M1 = np.random.rand(2,3)
M2 = np.random.rand(3,4)
res = [[sum([M1[i][k] * M2[k][j] for k in range(M1.shape[1])]) for j in range(M2.shape[1])] for i in range(M1.shape[0])]
(np.abs((M1@M2 - res) < 1e-15)).all()
# NumPy实际计算矩阵乘法更推荐：
# M1 @ M2
# 或 np.dot(M1,M2)
# 这里手写循环主要为了理解矩阵乘法内部逻辑


#=================================
'''Ex2：更新矩阵'''
np.random.seed(0)
A = np.random.randint(10, 20, (8, 5))
对于矩阵A：
# Bij = Aij * Σ(1/Aik)
# 其中k遍历当前行所有元素
理解：
每一行计算一个系数。
例如：
第一行：
[1,2,3]
先计算：
1/1 + 1/2 + 1/3
得到一个固定值。
然后：
这一行每个元素 × 这个固定值。
所以：
每一行对应一个乘数。
"""
A = np.arange(1,10).reshape(3,-1)
# 方法：
# A.sum(1)
#
# 对每一行求和
B = A * (1/A).sum(1).reshape(-1,1)
print(B)
"""
重点：
reshape(-1,1)
作用：
把一维数组变成列向量。
例如：
[1,2,3]
变成：
[
[1],
[2],
[3]
]
方便和矩阵进行广播。


#================================
Ex3：NumPy广播机制与卡方统计量
题目：
理解不同维度数组之间的自动扩充。
核心：
NumPy不会真正复制数据，
而是按照规则扩展维度。
例如：
(3,2)乘(2,)
第二个数组会看成：
[
[2,3],
[2,3],
[2,3]
]
然后逐元素相乘。
注意：
这不是矩阵乘法！
只是对应位置相乘。
"""
res = np.ones((3,2))

print(res * np.array([2,3]))
"""
重点：
理解广播规则：
从最后一个维度开始匹配。
如果长度一致，
或者其中一个为1，
可以广播
参考答案：
np.random.seed(0)
A = np.random.randint(10, 20, (8, 5))
B = A.sum(0)*A.sum(1).reshape(-1, 1)/A.sum()
res = ((A-B)**2/B).sum()
res


#==============================
Ex4：改进矩阵计算的性能
题目：
优化矩阵距离计算。
原始方法及代码：
'''
np.random.seed(0)
m, n, p = 100, 80, 50
B = np.random.randint(0, 2, (m, p))
U = np.random.randint(0, 2, (p, n))
Z = np.random.randint(0, 2, (m, n))
def solution(B=B, U=U, Z=Z):
    L_res = []
    for i in range(m):
        for j in range(n):
            norm_value = ((B[i]-U[:,j])**2).sum()
            L_res.append(norm_value*Z[i][j])
    return sum(L_res)
solution(B, U, Z)
'''
双循环：
for i:
    for j:
逐个计算距离。
缺点：
数据量大时速度慢。
优化思想：
利用矩阵公式：
||Bi-Uj||²
展开：
Bi² + Uj² - 2BiUj
转换为：
矩阵整体计算。
"""
np.random.seed(0)
m,n,p = 100,80,50
B = np.random.randint(0,2,(m,p))
U = np.random.randint(0,2,(p,n))
Z = np.random.randint(0,2,(m,n))
Y = (
    (B**2).sum(1).reshape(-1,1)    # B每一行平方和:   # shape=(m,),reshape(-1,1),变成(m,1),才能和Y矩阵(m,n)广播
    +
    (U**2).sum(0)
    -
    2*B@U
)
result = (Y*Z).sum()
print(result)
"""
核心理解：
不是减少计算，
而是把：
大量Python循环
转换成：
NumPy底层矩阵计算。
这就是数据分析和机器学习常用思想。


#===========================
#Ex5：连续整数的最大长度
"""
题目：
输入一个整数的Numpy数组，返回其中严格递增连续整数子数组的最大长度，正向是指递增方向。
例如，输入[1,2,5,6,7]，[5,6,7]为具有最大长度的连续整数子数组，因此输出3；输入[3,2,1,2,3,4,6]，[1,2,3,4]为具有最大长度的连续整数子数组，因此输出4。
请充分利用Numpy的内置函数完成。（提示：考虑使用nonzero, diff函数）
例如：
[1,2,5,6,7]
连续：
[1,2]
长度2
[5,6,7]
长度3
"""
def longest_length(x):
    """
    思路：
    1.
    np.diff计算相邻差值
    2.
    连续整数：
    差值必须等于1
    3.
    找到不等于1的位置作为断点
    4.
    计算断点之间距离
    5.
    最大值就是最长长度
    """
    return np.diff(
        np.nonzero(
            np.r_[1,np.diff(x)!=1,1] #两端补1： 防止第一个连续段和最后一个连续段无法计算长度,例如：[True,False,True]中间False的位置就是断点
        )
    ).max()
print(longest_length(np.array([1,2,5,6,7])))
"""
重点理解：
不要直接寻找连续数字。
转换思维：
连续问题
↓
寻找断点问题
这是数组算法的重要思想。"""
参考答案：
f = lambda x:np.diff(np.nonzero(np.r_[1,np.diff(x)!=1,1])).max()
f([1,2,5,6,7])
f([3,2,1,2,3,4,6])













