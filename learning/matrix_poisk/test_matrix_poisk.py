import unittest
from matrix_poisk import find_number

class TestMatrixPoisk(unittest.TestCase):
    def test_find_number(self):
        self.assertEqual(find_number(8,self.matrix),[[2,2]])

    def setUp(self):
        self.matrix=[[0,1,2],[3,4,5],[6,7,8]]


if __name__=="__main__":
    unittest.main()