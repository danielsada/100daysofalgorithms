""""
Middle of the LinkedList (easy)


Problem Statement

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
"""
import unittest

class Node():
    def __init__(self, node = None, value = None):
        self.next = node
        self.value = value
    def __repr__(self) -> str:
        return f"Node value: {self.value}"


def find_middle_linked_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    return slow.value

class TestLinkedList(unittest.TestCase):
    def test_linkedlist(self):
        linkedList = Node(Node(Node(Node(Node(None, 1), 2), 3), 4), 5)
        self.assertEqual(find_middle_linked_list(linkedList), 3)


