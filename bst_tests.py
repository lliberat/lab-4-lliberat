import unittest
from bst import *

def func():
    pass

def func2(arg,arg2):
    return(arg<arg2)

class TestCase(unittest.TestCase):

    def test_init(self):
        b = BinarySearchTree(None,None,12,func())
        self.assertEqual(b.value,12)
        self.assertEqual(b.left, None)
        self.assertEqual(b.right, None)
        self.assertEqual(b.func, func())


    def test_eq(self):
        b = BinarySearchTree(None,None,12,func())
        self.assertEqual(b,BinarySearchTree(None,None,12,func()))

    def test_repr(self):
        b = BinarySearchTree(None,None,12,func())
        self.assertEqual(b.__repr__(),"BinarySearchTree(None, None, 12, fuinc())")

    def test_isempty(self):
        b = None
        self.assertTrue(is_empty(b))


    def test_isnert(self):
        b = BinarySearchTree(BinarySearchTree(BinarySearchTree(None,None,7,func2(left,right)),None,8,func()),BinarySearchTree(None,None,11,func()),10,func())
        w = insert(b,6)
        self.assertEqual()

    def test_get(self):
        L = List([0, 1, 2, 3, 4, 5, None], 6, 7)
        with self.assertRaises(IndexError):
            get(L,12)
        self.assertEqual(get(L,1),1)

    def test_set(self):
        L = List([0, 1, 2, 3, 4, 5, None], 6, 7)
        with self.assertRaises(IndexError):
            set(L,12,25)

        self.assertEqual(set(L,0,12),List([12,1,2,3,4,5,None],6,7))

    def test_remove(self):
        L = List([0, 1, 2, 3, 4, 5, None], 6, 7)
        with self.assertRaises(IndexError):
            remove(L,12)
        self.assertEqual(remove(L,0),(0,List([1,2,3,4,5,None],5,7)))


if __name__ == '__main__':
    unittest.main()