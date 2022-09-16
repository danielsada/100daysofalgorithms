""""
Reverse Linkedlist

Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
"""
import unittest

class Node():
    def __init__(self, node = None, value = None):
        self.next = node
        self.value = value
    def __repr__(self) -> str:
        return f"Node value: {self.value}"

# returns head of reversed linkedlist
def reverse(head):
    curr = head
    prevNode, nextNode = None, None
    while curr is not None:
        nextNode = curr.next
        curr.next = prevNode
        prevNode = curr
        curr = nextNode
    return prevNode.value

class TestReverse(unittest.TestCase):
    def test_linkedlist(self):
        linkedList = Node(Node(Node(Node(Node(None, 1), 2), 3), 4), 5)
        self.assertEqual(reverse(linkedList), 1)


