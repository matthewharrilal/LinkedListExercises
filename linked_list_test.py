from linked_list import LinkedList, Node
import unittest



class LinkedListTest(unittest.TestCase):
    # def test_init(self):
    #     ll = LinkedList()
    #     assert ll.head is None
    #     assert ll.tail is None
    #     assert ll.size == 0
    #
    # def test_init_with_list(self):
    #     ll = LinkedList(['A', 'B', 'C'])
    #     assert ll.head.data == 'A'  # first item
    #     assert ll.tail.data == 'C'  # last item
    #     assert ll.size == 3

    # def test_append(self):
    #     ll = LinkedList()
    #     assert ll.size == 0
    #     ll.append('A')
    #     assert ll.size == 1
    #     ll.append('B')
    #     assert ll.size == 2
    #     ll.append('C')
    #     ll.append('D')
    #     assert ll.size == 4

    def test_reverse_linked_list_iterative(self):
        ll = LinkedList()
        ll.append('A')
        ll.append('B')
        ll.append('C')
        assert ll.size == 3
        ll.reverse_linked_list_iterative()
        assert ll.get_at_index(0) == 'C'
        assert ll.get_at_index(1) == 'B'
        assert ll.tail.data == 'A'