#  ==============
#  np数组的变形与合并
#  ==============
import numpy as np
# 转置：T
np.zeros((2,3)).T
#合并操作：r_, c_
#对于二维数组而言，r_和c_分别表示上下合并和左右合并：
np.r_[np.zeros((2,3)),np.zeros((2,3))]
np.c_[np.zeros((2,3)),np.zeros((2,3))]
# 一维数组和二维数组进行合并时，应当把其视作列向量，在长度匹配的情况下只能够使用左右合并的c_操作
try:
     np.r_[np.array([0,0]),np.zeros((2,1))]
except Exception as e:
     Err_Msg = e
Err_Msg
np.r_[np.array([0,0]),np.zeros(2)]#np.zeros(2)：创建一个长度为2的一维数组，里面全部是0
np.c_[np.array([0,0]),np.zeros((2,3))]#np.array([0,0])， c_会把一维数组转换成列向量，再进行左右拼接

#维度变换：reshape
#reshape把原数组按照新的维度重新排列。分别为C模式和F模式，分别以逐行和逐列的顺序进行填充读取
target = np.arange(8).reshape(2,4)# 把原来的一维变成2X4的矩阵
target
target.reshape((4,2), order='C') # 按照行读取和填充
'''运行结果：array([[0, 1],
                 [2, 3],
                 [4, 5],
                 [6, 7]])  '''
target.reshape((4,2), order='F') # 按照列读取和填充
'''array([[0, 2],
       [4, 6],
       [1, 3],
       [5, 7]])'''
#特别地，由于被调用数组的大小是确定的，reshape允许有一个维度存在空缺，此时只需填充-1即可：
target.reshape((4,-1))# -1意为把原来的变为4行，但是用户不一定知道列数，填-1让python自己计算
# 下面将n*1大小的数组转为1维数组的操作是经常使用的：
target = np.ones((3,1))
target
target.T
target.reshape(-1)# # reshape(-1)可以把n×1数组变为一维数组
# 注意.T只是转置，不会降低维度


# ==============
# np数组的切片与索引
# ==============
#数组的切片模式支持使用slice类型的start:end:step切片，还可以直接传入列表指定某个维度的索引进行切片
target = np.arange(9).reshape(3,3)
target
target[:-1, [0,2]]# :-1表示从第0行开始取，不要最后一行；没有冒号表示取最后一行
# 此外，还可以利用np.ix_在对应的维度上使用布尔索引，但此时不能使用slice切片：
target[np.ix_([True, False, True], [True, False, True])]#  第一个[]是对应行取不取，第二个[]是对应列
target[np.ix_([1,2], [True, False, True])]
# 当数组维度为1维时，可以直接进行布尔索引，而无需np.ix_：
new = target.reshape(-1)
new[new%2==0]


# ======
# 常用函数
# ======

#1.where是一种条件函数，可以指定满足条件与不满足条件位置对应的填充值：
a = np.array([-1,1,-1,0])
np.where(a>0, a, 5) # 对应位置为True时填充a对应元素，否则填充5
#  输出：array([5, 1, 5, 5])

#2.nonzero返回非零数的索引，argmax, argmin分别返回最大和最小数的索引
a = np.array([-2,-5,0,1,3,-1])
np.nonzero(a) #array([0, 1, 3, 4, 5])
a.argmax()# 4
a.argmin()# 1

# 3.any指当序列至少 存在一个 True或非零元素时返回True，否则返回False
#all指当序列元素 全为 True或非零元素时返回True，否则返回False
a = np.array([0,1])
a.any()# True
a.all()# False

# 4.cumprod, cumsum分别表示累乘和累加函数，返回同长度的数组，diff表示和前一个元素做差，由于第一个元素为缺失值，因此在默认参数情况下，返回长度是原数组减1
a = np.array([1,2,3])
a.cumprod()# array([1, 2, 6], dtype=int32)
a.cumsum()# array([1, 3, 6], dtype=int32)
np.diff(a)# array([1, 1])

# 5.常用的统计函数包括max, min, mean, median, std, var, sum, quantile，其中分位数计算是全局方法，因此不能通过array.quantile的方法调用：
target = np.arange(5)
target
target.max()# 输出4
np.quantile(target, 0.5) # 0.5分位数意思就是中位数 输出：2.0
# 但是对于含有缺失值的数组，它们返回的结果也是缺失值，如果需要略过缺失值，必须使用nan*类型的函数，上述的几个统计函数都有对应的nan*函数。
target = np.array([1, 2, np.nan])
target     #  array([ 1.,  2., nan])
target.max()  # 输出nan
np.nanmax(target)  # 意思是不包括nan  输出2.0
np.nanquantile(target, 0.5)  #输出1.5
#协方差和相关系数分别利用cov, corrcoef
target1 = np.array([1,3,5,9])
target2 = np.array([1,5,3,-9])
np.cov(target1, target2)
np.corrcoef(target1, target2)
#   二维Numpy数组中统计函数的axis参数，它能够进行某一个维度下的统计特征计算，当axis=0时结果为列的统计指标，当axis=1时结果为行的统计指标：
target = np.arange(1,10).reshape(3,-1)
target
'''输出array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])'''
target.sum(0) # 输出array([12, 15, 18])  axis=0，表示竖着切,沿列方向统计，结果为每列的统计值
target.sum(1) # 输出array([ 6, 15, 24])  axis=1，表示横着切,沿行方向统计，结果为每行的统计值


#=========
#  广播机制
#=========
#  标量和数组的操作
# 当一个标量和数组进行运算时，标量会自动把大小扩充为数组大小，之后进行逐元素操作
res = 3 * np.ones((2,2)) + 1
res
np.ones((2, 2))
res = 1 / res
res

a=np.array([[2,3]])# 一维数组
#  二维数组之间的操作
res = np.ones((3,2))
res
res * np.array([[2,3]]) # 第二个数组扩充第一维度为3，[2,3]先被看作是（2，），第一维是行
#   输出为array([[2., 3.],
#              [2., 3.],
#              [2., 3.]])
res * np.array([[2],[3],[4]]) # 第二个数组扩充第二维度为2，第二维是列,(3,1)数组扩充列方向，使其变成(3,2)
#array([[2., 2.],
#       [3., 3.],
#      [4., 4.]])
res * np.array([[2]]) # 等价于两次扩充，第二个数组两个维度分别扩充为3和2
#array([[2., 2.],
#       [2., 2.],
#       [2., 2.]])

e = np.ones(3)
# 一维数组与二维数组的操作
np.ones(3) + np.ones((2,3)) #扩充方式一样
#array([[2., 2., 2.],
#       [2., 2., 2.]])
np.ones(3) + np.ones((2,1)) #两个都需要扩充
#array([[2., 2., 2.],
#       [2., 2., 2.]])
np.ones(1) + np.ones((2,3))
#array([[2., 2., 2.],
#       [2., 2., 2.]])


#=============
#向量与矩阵的计算
#=============
a = np.arange(4).reshape(-1,2)
a
b = np.arange(-4,0).reshape(-1,2)
b
a@b