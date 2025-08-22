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
    i, j = 0, len(arr) - 1
    while i < j:
        i += 1
        j -= 1


# Linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycles(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    if fast == slow:  # Cycle!
        return fast


def reverse_linked_list(head):
    previous, current, Next = None, head, None
    while current is not None:
        Next = current.next
        current.next = previous
        previous = current
        current = Next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next.next
str(find_cycles(head).value)

from collections import deque


class TreeNode:
    value = None
    left, right = None, None

    def __init__(self, value, left=None, right=None) -> None:
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
    i -= 1
    print(queue)
    item = queue.popleft()
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

# Stacks in python
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
first_element = q.popleft()

# Heaps in python
import heapq

# minheap

stack = []
heapq.heappush(stack, 1)
heapq.heappush(stack, 10)
heapq.heappush(stack, 100)
print(stack)
# [1, 10, 100]
heapq.heappush(stack, 123)
heapq.heappush(stack, 1524)
print(stack)
# [1, 10, 100, 123, 1524]
heapq.heappush(stack, 20)
print(stack)
# [1, 10, 20, 123, 1524, 100]

heapq.heappop(stack)
# 1
heapq.heappop(stack)
# 10
heapq.heappop(stack)
# 20
print(stack)
# [100, 123, 1524]

# maxheap

# insert negatives
stack = []
heapq.heappush(stack, -1)
heapq.heappush(stack, -10)
heapq.heappush(stack, -100)
print(stack)
# [-100, -1, -10]
heapq.heappush(stack, -123)
heapq.heappush(stack, -12300)
heapq.heappush(stack, -15)
print(stack)
# [-12300, -123, -15, -1, -100, -10]

# Level ordering


class TreeNode:
    value = None
    left, right = None, None

    def __init__(self, value, left=None, right=None) -> None:
        self.left, self.right = left, right
        self.value = value

    def __repr__(self) -> str:
        return f"Node value: {self.value}"


node = TreeNode(4)
node.left = TreeNode(5, TreeNode(6), TreeNode(7))
node.right = TreeNode(10)


def print_levels(node: TreeNode):
    if node is None:
        return
    queue: list[TreeNode] = [node]
    while queue:
        levelsize = len(queue)
        for _ in range(levelsize):
            node = queue.pop(0)
            print(f"{node.value} ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


print_levels(node)

# Subsets
find_all_subsets = [1, 3, 5]
found = []
found.append([])

for e in find_all_subsets:
    temp_sets = []
    n = len(found)
    for i in range(n):
        newset = list(found[i])
        newset.append(e)
        found.append(newset)

print(found)

# permutations

nums = [1, 4, 5, 6, 20]
numsLength = len(nums)
result = []
permutations = deque()
permutations.append([])

for currentNumber in nums:
    n = len(permutations)
    for _ in range(n):
        currLenPermutation = permutations.popleft()
        for j in range(len(currLenPermutation) + 1):
            newPerm = list(currLenPermutation)
            newPerm.insert(j, currentNumber)
            if len(newPerm) == numsLength:
                result.append(newPerm)
            else:
                permutations.append(newPerm)

print(permutations)

# Tries


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.isEnd = False  # Flag to represent end of a word.


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_to_trie(self, word: str):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
        node.isEnd = True

    def search(self, word: str):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.isEnd

    def startswith(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
