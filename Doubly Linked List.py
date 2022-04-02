class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev                     # reference to prev node
            self._next = next                     # reference to next node



    def __init__(self):
        """Create an empty linkedlist."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        return self._head._next._element              # front aligned with head of list

    def last(self):
        """Return (but do not remove) the element at the end of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        return self._tail._prev._element


    def delete_first(self):
        """Remove and return the first element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        return self._delete_node(self._head._next)

    def delete_last(self):
        """Remove and return the last element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        return self._delete_node(self._tail._prev)


    def add_first(self, e):
        """Add an element to the front of list."""
        self._insert_between(e, self._head, self._head._next)


    def add_last(self, e):
        """Add an element to the back of list."""
        self._insert_between(e, self._tail._prev, self._tail)


    def __str__(self):
        result = ['head <--> ']
        curNode = self._head._next
        while (curNode._next is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)

    def split_after(self, index):
        """
        :index: Int -- split after this indexed node.
        (index start from zero)

        split self DoubleLinkedList into two separate lists.

        ***head/tail sentinel nodes does not count for indexing.

        :return: A new DoubleLinkedList object that contains the second section.
        """

        curr = self._head._next
        for i in range(index):
            curr = curr._next
        otherlist = DoubleLinkedList()
        curr2 = curr._next
        curr._next = self._tail
        self._tail._prev = curr

        while curr2._element != None:
            otherlist.add_last(curr2._element)
            curr2 = curr2._next
        
        self._size = index+1
        return otherlist

    def merge(self, otherlist):
        """
        :otherlist: DoubleLinkedList -- another DoubleLinkedList to merge.

        For example:
        L1: head<-->1<-->2<-->3-->tail
        L2: head<-->4-->tail
        L1.merge(L2)
        L1: head<-->1-->2-->3<-->4-->tail
        L2: head<-->tail
        :return: Nothing.
        """

        while not otherlist.is_empty():
            element = otherlist.delete_first()
            print(element)
            self.add_last(element)

def main():
    import random
    test_list = DoubleLinkedList()
    for i in range(8):
        test_list.add_first(random.randint(0, 20))
    print("Test list length 8, looks like:")
    print(test_list)
    print("--------------------------------------------------------")
    print("Split after index 5:")
    new_list = test_list.split_after(5)
    print("Original List:", test_list)
    print("The second part:", new_list)
    print("--------------------------------------------------------")
    print("Merging original list with the second part:")
    test_list.merge(new_list)
    print("Original List:", test_list)
    print("The second part:", new_list)
    print("--------------------------------------------------------")

if __name__ == '__main__':
    main()

