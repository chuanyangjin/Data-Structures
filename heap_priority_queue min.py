class HeapPriorityQueue:
    """A min-oriented priority queue implemented with a binary heap."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)

    #------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)     # index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)    # index beyond end of list?
    
    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)             # recur at position of parent
    
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left               # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)    # recur at position of small child

    ## Bottom_Up Heap Construction ##
    def _heapify(self):
        start = self._parent(len(self)-1)
        for j in range(start, -1, -1):
            self._downheap(j)
    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    ## This part is only for testing _heapify function ##
    def __init__(self, contents=[]):
        """Create a new empty Priority Queue."""
        self._data = [self._Item(k,v) for k,v in contents]
        if len(self._data)>1:
            self._heapify()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)            # upheap newly added position
    
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)           # put minimum item at the end
        item = self._data.pop()                      # and remove it from the list;
        self._downheap(0)                            # then fix new root
        return (item._key, item._value)

if __name__ == '__main__':
    heap = HeapPriorityQueue()
    import random
    for i in range(10):
        heap.add(random.randint(0, 20), "happy_final!")
    print(heap._data)

    for i in range(10):
        print("Removing from heap:", heap.remove_min()[0])

    ## Test _heapify ##
    contents=[(16,"Beijing"),(9,"Hangkong"),(15,"Shenzhen"),(7,"Guangzhou"),
              (8,"Chengdu"),(11,"Chongqing"),(2,"Suzhou")]
    heap = HeapPriorityQueue(contents)
    print(heap._data)
