from linked_list import Node


class Stack:

    def __init__(self):
        self.__head = None

    def push(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def pop(self):
        if not Stack.is_empty(self):
            node = self.__head
            self.__head = self.__head.next
            return node.value

    def is_empty(self):
        return self.__head is None


stack = Stack()
print(stack.pop())
stack.push(55)
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())




