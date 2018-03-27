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
        self.pq = [None] * (maxN+1)
        self.qp = [-1] * (maxN+1)
        self.keys = [None] * (maxN+1)
        self.maxN = maxN
        self.n = 0

    def __len__(self):
        return self.n

    def contains(self, i):
        return self.qp[i] != -1

    def insert(self, i, item):
        assert(i > 0 and i < self.maxN)
        if self.contains(i):
            raise "Already contains string"
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
        assert minE == self.pq[self.n+1]
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
        self.exch(index, n)
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def swim(self, k):
        while k > 0 and self.greater((k - 1) // 2, k):
            self.pq[k], self.pq[
                (k - 1) // 2] = self.pq[(k - 1) // 2], self.pq[k]
            k = (k - 1) // 2

    def sink(self, k):
        N = len(self.pq)
        while 2 * k + 1 <= N - 1:
            j = 2 * k + 1
            if j < N - 1 and self.greater(j, j + 1):
                j += 1

            if not self.greater(k, j):
                break

            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j
