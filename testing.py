import unittest
from sorted_linked_list import SortedLinkedList


class MyTestCase(unittest.TestCase):
    linky = SortedLinkedList()

    def test_to_array(self):
        self.linky.append(4)
        self.assertEqual(self.linky.to_array(), [4])  # add assertion here

    def test_remove(self):
        self.linky.append(666)
        self.linky.append(444)
        self.linky.remove(666)
        self.assertEqual(self.linky.to_array(), [444])

    def test_is_exist(self):
        self.linky.append(444)
        self.assertTrue(self.linky.is_exist(444))


if __name__ == '__main__':
    unittest.main()
