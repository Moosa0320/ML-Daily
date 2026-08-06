from my import add, sub
import unittest

class UnitTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(add(5,6),11)

    def testSub(self):
        self.assertEqual(sub(6,2),4)


if __name__ == '__main__':
    unittest.main()