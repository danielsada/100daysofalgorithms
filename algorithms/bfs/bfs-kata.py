from collections import deque
from typing import List

class Node:
    value = None
    left, right = None, None
    def __init__(self, value,  left = None, right = None) -> None:
        self.left, self.right = left, right
        self.value = value
    def __repr__(self) -> str:
        return f"Node value: {self.value}"


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

## BFS
queue = deque()
queue.append(root)
i = 10
while len(queue) > 0 and i >= 0:
    i -= 1;
    print(queue)
    item = queue.popleft();
    print(item)
    if item.left is not None:
        queue.append(item.left)
    if item.right is not None:
        queue.append(item.right)
    
print("PREORDER")
## DFS, preorder
def explore(curr):
    print(curr)
    if curr.left is not None:
        explore(curr.left)
    if curr.right is not None:
        explore(curr.right)

explore(root)

print("POSTORDER")

## DFS, postorder:
def explore_post(curr):
    if curr.left is not None:
        explore_post(curr.left)
    if curr.right is not None:
        explore_post(curr.right)
    print(curr)


explore_post(root)