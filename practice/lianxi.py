'''import numpy as np
np.random.seed(0)
res = np.random.rand(4,4)
A = 1 / res
B = np.zeros((4,4))
for i in range(A.shape[0]):
    item = 0
    for j in range(A.shape[1]):
        item += A[i][j]
    C = item
    for j in range(A.shape[1]):
        B[i][j] = res[i][j]*C
print(B)'''


'''
A = np.arange(1,10).reshape(3,-1)
B = A*(1/A).sum(1).reshape(-1,1)
B
print(A)
print(B)


import numpy as np
A = np.arange(1,10).reshape(3,-1)
print(A)
B = (A.sum(1).reshape(3,-1)*A.sum(0))/(A.sum())
print(B)'''

import numpy as np
np.random.seed(0)
m, n, p = 100, 80, 50
B = np.random.randint(0, 2, (m, p))
U = np.random.randint(0, 2, (p, n))
Z = np.random.randint(0, 2, (m, n))
print(B[i])
'''
def solution(B=B, U=U, Z=Z):
    L_res = []
    for i in range(m):
        for j in range(n):
            norm_value = ((B[i]-U[:,j])**2).sum()
           
            print(B[i])
            L_res.append(norm_value*Z[i][j])
    return sum(L_res)
solution(B, U, Z)
print(solution(B, U, Z))'''

def solution(B=B, U=U, Z=Z):
    solution(B, U, Z) = ((B[i]-U[:,j])**2).sum()*Z[i][j]
print(solution(B, U, Z))



np.nonzero(a)
np.diff(a)