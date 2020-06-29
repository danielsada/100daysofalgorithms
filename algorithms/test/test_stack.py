import unittest
from algorithms.stack.stack_parenthesis_check import StackParenthesisCheck

__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"

"""
Test the syntax for parenthesis. 
"""


class TestStackParenthesis(unittest.TestCase):
    def setUp(self):
        self.a = StackParenthesisCheck("()()(){[]}")
        self.b = StackParenthesisCheck("()(()){[]}<")
        self.c = StackParenthesisCheck("<<<<<<")

    def test_stack_correct(self):
        self.assertTrue(self.a.isSyntaxCorrect)

    def test_stack_incorrect(self):
        self.assertFalse(self.b.isSyntaxCorrect)

    def test_stack_incorrect_justOpen(self):
        self.assertFalse(self.c.isSyntaxCorrect)
