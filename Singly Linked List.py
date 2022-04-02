class SingleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._next = next                     # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        return self._head._element              # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Exception('list is empty')
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def return_max(self):
        """
        return the maximum element stored with in self.

        For example, 9 --> 5 --> 21 --> 1 --> None should return 21. 
        :return: The maximum element.
        """ 
        curr = self._head
        maxi = self._head._element
        while curr._next != None:
            curr = curr._next
            if curr._element > maxi:
                maxi = curr._element
        return maxi

    def __iter__(self):
        """
        generate a forward iteration of the elements from self list.

        In other words, for each in SingleLinkedList object will become working.

        :return: No return. Use yield instead.
        """
        curr = self._head
        yield curr._element
        while curr._next != None:
            curr = curr._next
            yield curr._element

    def insert_after_kth_index(self, k, e):
        """
        :param k: Int -- insert after this indexed node.
        :param e: Any -- the value we are storing
    
        Insert element e (as a new node) after kth indexed node in self linkedlist.
        (index start from zero)

        L1: 11-->22-->33-->44-->None
        L1.insert_after_kth_index(2, "Hi")
        L1: 11-->22-->33-->”Hi”-->44-->None

        :return: Nothing.
        """
        curr = self._head
        for i in range(k):
            curr = curr._next
        new_node = self._Node(e, curr._next)
        curr._next = new_node 
        # new_node._next = curr._next -- MemoryError (Infinite Loop)
        self._size += 1

    def unOrderedSearch(self,target):
        # Search for the target element in the Linked List
        # to do
        if self.is_empty():
            raise Exception('LinkedList is empty')
        current_node = self._head
        index = 0
        if self._head._element == target:
            return index
        while current_node._next is not None:
            current_node = current_node._next
            index += 1
            if current_node._element == target:
                return index
        return False


def main():
    import random
    test_list = SingleLinkedList()
    for i in range(8):
        test_list.insert_from_head(random.randint(0, 20))
    print("Test list length 8, looks like:")
    print(test_list)
    print("--------------------------------------------------------")
    print("Maximum value within test list:", test_list.return_max())
    print("--------------------------------------------------------")
    print("Testing __iter__ ............")
    for each in test_list:
        print(each, end = " ")
    print()
    print("--------------------------------------------------------")
    print("Testing insert_after_kth_index ............")
    test_list.insert_after_kth_index(3, "Hi")
    print(test_list)
    print("--------------------------------------------------------")
    print(test_list.unOrderedSearch(15))

if __name__ == '__main__':
    main()

