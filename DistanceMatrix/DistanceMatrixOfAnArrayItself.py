# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
# 向量矩阵为：
# [[1, 2],
#  [3, 4],
#  [5, 6],
#  [7, 8]]
A = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8]])
# distA距离列表为（上三角矩阵展开成一个列表）:
# [2.828, 5.656, 8.485, 2.828, 5.656, 2.828]
distA = pdist(A, metric='euclidean')
# 将distA数组变成一个矩阵
# distB距离矩阵为:
# [[0,     2.828, 5.656, 8.485],
#  [2.828, 0,     2.828, 5.656],
#  [5.656, 2.828, 0,     2.828],
#  [8.485, 5.656, 2.828, 0    ]]
distB = squareform(distA)