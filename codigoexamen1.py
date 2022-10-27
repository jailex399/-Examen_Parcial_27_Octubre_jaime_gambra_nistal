from typing import Any

class Stack:
    def __init__(self):
        self.data = []



    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def push(self, value: Any) -> None:
        self.data.append(value)

    def pop(self) -> Any:
        return self.data.pop()

    def __str__(self) -> str:
        return str(self.data)

    def __len__ (self):
        return len (self.data)


class Queue1:
    def __init__(self):
        self.data = []
        
    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False
        
    def enqueue(self, value: Any) -> None:
        self.data.insert(0, value)
    
    def dequeue(self) -> Any:
        return self.data.pop()
    
    def peek(self) -> Any:
        if not self.is_empty():
            return self.data[-1]
        return

from collections import deque

class Queue2:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()