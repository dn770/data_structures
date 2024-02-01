class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SortedLinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def append(self, value):
        node = Node(value)
        nd = self.__head

        if nd is None:  # empty list
            self.__head = node
            self.__tail = node

        else:
            while nd.next is not None and nd.next.value < node.value:
                nd = nd.next

            if nd.next is None:  # add to tail
                self.__tail.next = node
                self.__tail = self.__tail.next

            elif nd == self.__head:  # add to head
                if nd.value < node.value:  # 2nd
                    node.next = nd.next
                    nd.next = node
                else:  # minimum
                    node.next = nd
                    self.__head = node

            else:  # in the list
                node.next = nd.next
                nd.next = node

        self.__length += 1

    def is_exist(self, value):
        if not self.__head:
            return False
        node = self.__head
        while node is not None and node.value < value:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove(self, value):
        node = self.__head
        if node.value == value:
            self.__head = node.next
            self.__length -= 1
        else:
            while node.next is not None:
                if node.next.value != value:
                    node = node.next
                else:
                    node.next = node.next.next
                    self.__length -= 1

    def clear(self):
        self.__head = None
        self.__tail = self.__head

    def to_array(self):
        nodes_arr = []
        node = self.__head
        while node:
            nodes_arr.append(node.value)
            node = node.next
        return nodes_arr

    def __str__(self):
        sll_str = ""
        node = self.__head
        while node:
            sll_str += str(node.value)
            sll_str += " "
            node = node.next
        return sll_str


if __name__ == "__main__":

    linky = SortedLinkedList()
    for i in range(5):
        linky.append(i * 3)
        linky.append(-i)
    linky.remove(0)
    print(linky.to_array())
