import unittest
import typing
def countIslandsDFS(matrix: list[list[int]]);
    rows, cols= len(matrix), 
    for i in range(rows):
        for j in range(cols):
            countIslandsDFSRecursionHelper(i, j)

def countIslandsDFSRecursionHelper()


class IslandTest(unittest.TestCase):
    def TestCountIslands(self):
        self.assertEqual(countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        self.assertEqual(countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 3)
        self.assertEqual(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        self.assertEqual(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 3)
        self.assertEqual(countIslandsBFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        self.assertEqual(countIslandsBFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 3)