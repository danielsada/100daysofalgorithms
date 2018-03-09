
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "yo@danielsada.mx"


class SymbolTable:
    """"
    Creates a table of symbols.
    """

    def __init__(self, string):
        pass

    def put(self, elem: tuple):
        pass

    """Returns None if not present"""

    def get(self, key) -> tuple:
        pass

    def delete(self, key):
        pass

    def contains(self, key) -> bool:
        if(self.get(key) != None):
            return None
