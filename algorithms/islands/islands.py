import unittest
import typing

def countIslandsDFS(matrix: list[list[int]]):
    count = 0
    rows, cols= len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
              pass
            else:
              count += 1
              countIslandsDFSRecursionHelper(i, j, matrix);
    return count
    
def countIslandsDFSRecursionHelper(i, j, matrix):
  if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix):
    return;
  if matrix[i][j] == 1:
    matrix[i][j] = 0
    countIslandsDFSRecursionHelper(i+1, j, matrix)
    countIslandsDFSRecursionHelper(i-1, j, matrix)
    countIslandsDFSRecursionHelper(i, j+1, matrix)
    countIslandsDFSRecursionHelper(i, j-1, matrix)  


class IslandTest(unittest.TestCase):
    def test_countIslands(self):
        self.assertEqual(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        self.assertEqual(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 1]]), 4)        
        self.assertEqual(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]), 3)
