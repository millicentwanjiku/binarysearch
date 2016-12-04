"""Implementing Binary Search"""

class BinarySearch(list):
    """Class that implements binary search"""

    def __init__(self, a, b):
        """Create a list of length a, start element b and step b"""

        list.__init__(self)
        self.length = a
        begin = b
        end = a * b
        while begin <= end:
            self.append(begin)
            begin += b

    def search(self, target):
        """Do a binary search and return the number of iterations"""
        found = False
        begin = 0
        end = self.length - 1
        middle = (begin + end) // 2
        iterations = 0

        # Perform binary search
        if (target == self[begin]) or (target == self[end]) \
          or (target == self[middle]):
            return {
          'count': iterations,
          'index': self.index(target)
          }

        while begin < end and not found:

            middle = (begin + end) // 2

            if target == self[middle]:
                found = True
            else:
                iterations += 1
            if target > self[middle]:
                begin = middle + 1
            else:
                end = middle - 1

        if found:
            return {
          'count': iterations,
          'index': self.index(target)
          }
        else:
            return {
          'count': iterations,
          'index': -1
          }
