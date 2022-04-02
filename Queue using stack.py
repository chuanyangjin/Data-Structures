from Stack import ArrayStack

class QueueUsingStacks:
    def __init__(self):
        # Your code
        self._stack1 = ArrayStack()
        self._stack2 = ArrayStack()
        self._l = 0

    def __len__(self):
        # Your code
        return self._l

    def is_empty(self):
        # Your code
        return len(self) == 0

    def enqueue(self, elem): #O(1)
        # Your code
        self._stack1.push(elem)
        self._l += 1
        
    def dequeue(self): #O(1)*
        if not self._stack2.is_empty(): #O(1)
            return self._stack2.pop()
        
        # pop stack1 and push into stack2 (Now stack2 behaves as a queue)
        while not self._stack1.is_empty(): #O(n)
            self._stack2.push(self._stack1.pop())

        if not self._stack2.is_empty():
            return self._stack2.pop()
    
        raise Exception("Queue is empty")

    def first(self): #O(1)*
        if not self._stack2.is_empty(): #O(1)
            return self._stack2.top()
        
        # pop stack1 and push into stack2 (Now stack2 behaves as a queue)
        while not self._stack1.is_empty(): #O(n)
            self._stack2.push(self._stack1.pop())

        if not self._stack2.is_empty():
            return self._stack2.top()
    
        raise Exception("Queue is empty")


if __name__ == '__main__':
    q1 = QueueUsingStacks()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    print(q1.dequeue()) # Expect: 1
    print(q1.dequeue()) # Expect: 2
    print(q1.dequeue()) # Expect: 3
    print(q1.dequeue()) # Expect: 4
