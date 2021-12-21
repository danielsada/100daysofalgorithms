

"""
Get the Nth number of fibonacci
"""

from typing import List, MutableSet
from unittest import result

   

class Matrix:
    [staticmethod]
    def matrixMultiplication(a: List[List[int]], b:List[List[int]]):
        assert len(a[0]) == len(b)
        assert len(a) > 0
        assert len(b) > 0
        resulting_matrix = [[None for x in range(len(a))] for y in range(len(b[0]))]
        getColumn = lambda i, mat: [item[i] for item in mat]
        getDot = lambda a,b : sum([i*j for (i,j) in zip(a,b)])
        for i in range(len(a)):
            for j in range(len(b[0])):
                resulting_matrix[i][j] = getDot(a[i],getColumn(j, b))
                # print(f"Resulting {i}, {j} = {resulting_matrix[i][j]}")
        return resulting_matrix

        # [1,2,3] 1
        #         2
        #         3
        # [1,2    [2,0
        #  3,4]    1,2]

        # [0][0] = 1*2 + 2*1
        # [0][1] = 
        # [1][0]
        # [1][1]


def getNthFibbonaci(n: int):
    matrix = [
        [1,1],
        [1,0]
    ]


# getNthFibbonaci(2)
mat = Matrix.matrixMultiplication([[1,2,3]], [[4],[5],[6]])
mat = Matrix.matrixMultiplication([[4],[5],[6]],[[1,2,3]])

