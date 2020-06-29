
__author__ = "Daniel Sada"
__license__ = "MIT Licence"
__email__ = "hello@danielsada.tech"


class SuffixSort:
    """"
    Well, I tried to implement this, but slice in python is O(k)
    and java string.substring is O(1), so you have to make python
    magic to make this work.

    [IN DEPRECATED]
    """

    def __init__(self, bigString):
        self.s = bigString
        self.suffixSort(self.s)

    def suffixSort(self, bS):
        a = []
        for i in range(0, len(bS)):
            a.append(bS[i:])

        self.a = a
        print(a)


x = SuffixSort("LOREM IPSUM IPSUM DOLORES")
print(sorted(x.a))
