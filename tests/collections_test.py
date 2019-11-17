import unittest

from um.collections import binary_search_tree as bst


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.root = bst.Node(1)
        self.l1 = bst.Node(2)
        self.r1 = bst.Node(3)
        self.l2 = bst.Node(4)
        self.root.left = self.l1
        self.root.right = self.r1
        self.l1.left = self.l2

    def test_breadth_first_search(self):
        searched = self.root.breadth_first_search(4)

        self.assertIs(searched, self.l2)
        not_found = self.root.breadth_first_search(100)
        self.assertIsNone(not_found)

    def test_depth_first_search(self):
        searched = self.root.depth_first_search(3)
        self.assertIs(searched, self.r1)

        not_found = self.root.depth_first_search(100)
        self.assertIsNone(not_found)
