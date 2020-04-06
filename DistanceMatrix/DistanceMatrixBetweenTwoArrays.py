# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import cdist
# 行向量:A （3行2列）
# [[1,2],
#  [3,4],
#  [5,6]]
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
# 行向量:B （2行2列）
# [[1,2],
#  [3,4]]
B = np.array([[1, 2],
              [3, 4]])
# 得到矩阵C（3行2列），由A->B的距离，Cij代表A中都第i个向量到B中第j向量的距离
# [[0,      2.828],
#  [2.828 , 0    ],
#  [5.656 , 2.828]]
C = cdist(A, B, metric='euclidean')
