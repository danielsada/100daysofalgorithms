"""
This is a guidesheet for the most common patterns I've found while doing researching algorithms.
"""

def sliding_window(k, arr):
    window_start = 0
    for window_end in range(len(arr)):
        # Leftmost item
        arr[window_end]
        # Shorten the window
        window_start += 1

def two_pointers(arr):
    i,j = 0,len(arr)-1
    while i < j:
        i += 1
        j -= 1

# Linked list
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_cycles(head):
    slow, fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    if fast == slow: # Cycle!
        return fast

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next.next
str(find_cycles(head).value)

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

