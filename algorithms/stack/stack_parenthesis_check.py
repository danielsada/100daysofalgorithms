__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class StackParenthesisCheck:
    """"
    Implement a stack that checks if match of square brackets,
    tags and parenthesis match their level.
    Accepts <> () [] {}
    """

    def __init__(self, string):
        self.string = string
        self.stack = []
        self.isSyntaxCorrect = self.checkParenthesis(string)

    def checkParenthesis(self, string) -> bool:
        for char in string:
            if char == '{' or char == '[' or char == '<' or char == '(':
                self.stack.append(char)
            if char == '}':
                if len(self.stack) == 0 or self.stack.pop() != '{':
                    return False
            if char == ']':
                if len(self.stack) == 0 or self.stack.pop() != '[':
                    return False
            if char == '>':
                if len(self.stack) == 0 or self.stack.pop() != '<':
                    return False
            if char == ')':
                if len(self.stack) == 0 or self.stack.pop() != '(':
                    return False
        if len(self.stack) > 0:
            return False
        else:
            return True
