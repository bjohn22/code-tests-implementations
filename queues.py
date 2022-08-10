# queues.py

from collections import deque

class Queue:
    """
    Basic Queue
    """
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        """Adds element to the tail end(right)"""
        self._elements.append(element)

    def dequeue(self):
        """removes element from the head position, left"""
        return self._elements.popleft()




class QueueNew:
    """
    - make Queue iterable
    - report its length
    - optionally accept initial elements
    Note: The asterisk operator (*) is used
     to unpack all the values of an iterable that have not been assigned yet.
     see https://geekflare.com/python-unpacking-operators/
    """
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


    def enqueue(self, element):
        """Adds element to the tail end(right)"""
        self._elements.append(element)

    def dequeue(self):
        """removes element from the head position, left"""
        return self._elements.popleft()