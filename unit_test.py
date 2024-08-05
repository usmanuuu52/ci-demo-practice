import unittest
from app import add,sub,mul

class Mathtest(unittest.TestCase):

    
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)


    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-5, 5), 0)


    def test_sub(self):
        self.assertEqual(sub(4,5), 20)
        self.assertEqual(sub(-3,1),- 3)


if __name__=='__main__':
    unittest.main()



    