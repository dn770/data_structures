class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node
        self.__length += 1

    def append(self, value):
        node = Node(value)
        n = self.__tail
        if n is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = self.__tail.next
            self.__length += 1

    def is_exist(self, value):
        if self.__head is None:
            return False
        node = self.__head
        while node is not None:
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
        self.__length = 0

    def length(self):
        return self.__length

    def to_array(self):
        nodes_arr = []
        node = self.__head
        while node:
            nodes_arr.append(node.value)
            node = node.next
        return nodes_arr

    def __str__(self):
        ll_str = ""
        node = self.__head
        while node is not None:
            ll_str += str(node.value)
            ll_str += " "
            node = node.next
        return ll_str

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head):
        self.__head = head

linky = LinkedList()
for i in range(5):
    linky.append(i)
    linky.add(-i)
linky.remove(0)
print(linky.to_array())