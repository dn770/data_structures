from linked_list import Node

class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, value):
        node = Node(value)
        if self.__tail is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            self.__tail = node

    def dequeue(self):
        node = self.__head
        if self.__head is not None:
            if self.__head == self.__tail:
                self.__tail = self.__tail.next
            self.__head = self.__head.next
            return node.value

queue = Queue()
print(queue.dequeue())
queue.enqueue(55)
print(queue.dequeue())

