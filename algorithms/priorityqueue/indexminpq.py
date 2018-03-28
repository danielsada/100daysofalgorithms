"""
MIT License

Copyright (c) 2017 shellfly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


I took some methods for this class from https://github.com/shellfly/algs4-py

Modified by me aftewards.
"""


class IndexMinPQ:
    def __init__(self, maxN):
        self.pq = [0] * (maxN+1)
        self.qp = [-1] * (maxN+1)
        self.keys = [None] * (maxN+1)
        self.maxN = maxN
        self.n = 0

    def __len__(self):
        return self.n

    def contains(self, i):
        return self.qp[i] != -1

    def insert(self, i, item):
        if i < 0 or i >= self.maxN:
            raise "out of bounds in insert of indexminpq"
        if self.contains(i):
            raise Exception(f"Already contains string {item}")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = item
        self.swim(self.n)

    def minIndex(self):
        assert self.n != 0
        return self.pq[1]

    def minItem(self):
        assert self.n != 0
        return self.keys[self.pq[1]]

    def delMin(self):
        minE = self.pq[1]
        self.n -= 1
        self.exch(1, self.n)
        self.sink(1)
        assert minE == self.pq[self.n]
        self.qp[minE] = -1  # Delete
        self.keys[minE] = None
        self.pq[self.n+1] = -1
        return minE

    def itemOf(self, i):
        return self.keys[i]

    def changeItem(self, i, item):
        self.keys[i] = item
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def decreaseItem(self, i, item):
        self.keys[i] = item
        self.swim(self.qp[i])

    def delete(self, i):
        index = self.qp[i]
        self.n -= 1
        self.exch(index, self.n)
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1

    def exch(self, i, j):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def greater(self, i, j):
        if self.keys[self.pq[i]] is None:
            return False
        if self.keys[self.pq[j]] is None:
            return True
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def swim(self, k):
        while k > 1 and self.greater(k // 2, k):
            self.exch(k, k//2)
            k = k//2

    def sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self.greater(j, j+1):
                j += 1
            if not self.greater(j, j+1):
                break
            self.exch(k, j)
            k = j
