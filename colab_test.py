import unittest
from  linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_new_linked_list(self):
        '''Can create new linked list instance'''
        linked_list = LinkedList()
        self.assertIsNone(linked_list.head)
        self.assertEqual(linked_list.length(), 0)

    def test_can_add_first_element(self):
        linked_list = LinkedList()
        linked_list.add(5)
        self.assertEqual(linked_list.length(), 1)
        self.assertEqual(linked_list.head.value, 5)

    def test_can_add_second_element(self):
        '''can add 2 element'''
        linked_list = LinkedList()
        linked_list.add(5)
        linked_list.add(8)
        self.assertEqual(linked_list.length(), 2)
        self.assertEqual(linked_list.head.value, 8)
        self.assertEqual(linked_list.head.next.value, 5)

    def test_to_array_function(self):
        '''can return array of elements'''
        linked_list = LinkedList()
        self.assertListEqual(linked_list.to_array(), [])
        linked_list.add(1)
        linked_list.add(2)
        self.assertListEqual(linked_list.to_array(), [2, 1])

    def test_append_function(self):
        '''can append values to the end of this list'''
        linked_list = LinkedList()
        linked_list.append(666)
        linked_list.append(444)
        self.assertEqual(linked_list.to_array(), [666, 444])
    def test_remove_function(self):
      '''can remove specific value from the list'''
      linked_list = LinkedList()
      linked_list.append(666)
      linked_list.append(444)
      linked_list.remove(666)
      self.assertEqual(linked_list.to_array(), [444])
    def test_is_exist_function(self):
      '''can check if value is in the list'''
      linked_list = LinkedList()
      linked_list.append(5)
      self.assertTrue(linked_list.is_exist(5))
      self.assertFalse(linked_list.is_exist(9))

    def test_print_function_exists(self):
      '''can print the list'''
      linked_list = LinkedList()
      self.assertIsNone(print(linked_list))







unittest.main(argv=[''], verbosity=2, exit=False)
