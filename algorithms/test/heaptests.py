from algorithms.heaps.heap import Heap
from algorithms.heaps.minheap import MinHeap
from algorithms.heaps.maxheap import MaxHeap
from algorithms.priorityqueue.priorityqueue import PriorityQueue
import unittest


class TestHeaps(unittest.TestCase):
    def setUp(self):
        self.gHeap = Heap()
        self.mh = MinHeap()
        self.mxh = MaxHeap()
        self.mxht = MaxHeap(tupled=True)
        self.pq = PriorityQueue()

    def test_generic_heap(self):
        """
        Test indexes for this heaps
                    0
                  1        2
               3    4    5   6
              7 8  9
        """

        self.gHeap.elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(self.gHeap.has_right_index(0))
        self.assertTrue(self.gHeap.has_left_index(0))
        self.assertFalse(self.gHeap.has_parent(0))

        self.assertTrue(self.gHeap.has_right_index(2))
        self.assertTrue(self.gHeap.has_left_index(2))
        self.assertTrue(self.gHeap.has_parent(2))

        self.assertFalse(self.gHeap.has_right_index(4))
        self.assertTrue(self.gHeap.has_left_index(4))

    def test_min_heap(self):
        self.mh.push(50)
        self.mh.push(40)
        self.mh.push(20)
        self.mh.push(30)
        self.assertEqual(self.mh.pop(), 20)
        self.assertEqual(self.mh.pop(), 30)
        self.assertEqual(self.mh.pop(), 40)
        self.assertEqual(self.mh.pop(), 50)

    def test_max_heap(self):
        self.mxh.push(50)
        self.mxh.push(40)
        self.mxh.push(20)
        self.mxh.push(30)
        self.assertEqual(self.mxh.pop(), 50)
        self.assertEqual(self.mxh.pop(), 40)
        self.assertEqual(self.mxh.pop(), 30)
        self.assertEqual(self.mxh.pop(), 20)

    def test_tupled_queues(self):
        self.mxht.push((False, 3))
        self.mxht.push(("far", 1000))
        self.mxht.push(("wow", 100))
        self.assertEqual(self.mxht.pop(), ("far", 1000))
        self.assertEqual(self.mxht.pop(), ("wow", 100))
        self.assertEqual(self.mxht.pop(), (False, 3))

    def test_priority_queue(self):
        arr = [1, 200, 2, 3, 5, 6]
        for e in arr:
            self.pq.add(e)
        self.assertEqual(self.pq.pop(), 200)
        self.assertEqual(self.pq.pop(), 6)
        self.assertEqual(self.pq.pop(), 5)


if __name__ == '__main__':
    unittest.main()
