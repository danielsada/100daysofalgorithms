import unittest
from algorithms.fibonacci.fibonaccimatrixes import Matrix

class TestMatrixes(unittest.TestCase):
    def setUp(self):
        print("HELLO")
        
    def textMatrix(self):
        mat = Matrix.matrixMultiplication([1,2,3], [[1],[2],[3]])
        print(mat)
        self.assertTrue(len(mat) == 1)
        self.assertEqual(mat[0], 32)