
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"

import pandas as pd


class Simplex:
    """"
    Simplex algorithm for minimizing or maximising constraints
    """

    def __init__(self, a, b, c):
        """A is the array's  recipe for the problem.
            [M rows x N columns]
        B is the values that result given that recipe
            [M rows x 1 column],
        C is the maximize function
            [1 row x N columns]
            where:
                N is the number of variables.
                M is the number of constraints."""
        self.m = len(b)
        self.n = len(c)
        self.t = [[0 for i in range(self.m+self.n+1)] for j in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.t[i][j] = a[i][j]
        for j in range(self.n, self.n + self.m):
            self.t[j - self.n][j] = 1
        for j in range(self.n):
            self.t[self.m][j] = c[j]
        for i in range(self.m):
            self.t[i][self.m+self.n] = b[i][0]
        self.solve()
        print(pd.DataFrame(self.t))

    def solve(self):
        i = 0
        while(i < 1000):
            q = self.bland()
            if(q == -1):
                break
            p = self.minRatio(q)
            if(p == -1):
                break
            self.pivot(p, q)
            i += 1

    def bland(self) -> int:
        for q in range(self.m+self.n):
            if(self.t[self.m][q] > 0):
                return q
        return -1

    def minRatio(self, q) -> float:
        p = -1
        for i in range(self.m):
            if self.t[i][q] <= 0:
                continue
            elif p == -1:
                p = i
            elif (self.t[i][self.m+self.n] / self.t[i][q]) < (self.t[p][self.m+self.n] / self.t[p][q]):
                p = i
        return p

    def pivot(self, p, q):
        for i in range(self.m):
            for j in range(self.m + self.n):
                if i != p and j != q:
                    self.t[i][j] -= self.t[p][j] * self.t[i][q] / self.t[p][q]

        for i in range(self.m):
            if i != p:
                self.t[i][q] = 0.0

        for j in range(self.m+self.n):
            if j != q:
                self.t[p][j] /= self.t[p][q]
        self.t[p][q] = 1.0


import unittest


class SimplexTest(unittest.TestCase):
    def test_brewers(self):
        a = [[5, 15],
             [4, 4],
             [35, 20]]
        b = [[480],
             [160],
             [1190]]
        c = [13, 23]
        s = Simplex(a, b, c)


if __name__ == '__main__':
    unittest.main()
