import unittest
import ratio

class MyTest(unittest.TestCase):

    # Test normal bounds of ratio
    def test_ratioNorm1(self):
        testLst = [False] * 300 + [True] * 300
        self.assertEqual(ratio.getRatio(testLst), 1)

    def test_ratioNorm2(self):
        testLst = [True] * 300 + [False] * 300
        self.assertEqual(ratio.getRatio(testLst), 1)

    def test_ratioNorm3(self):
        testLst = [True, False, False] * 300
        self.assertEqual(ratio.getRatio(testLst), 0.5)

    # Test 0 edge cases
    def test_ratioZeroDen(self):
        testLst = [True]
        self.assertEqual(ratio.getRatio(testLst), 0)

    def test_ratioZeroNum(self):
        testLst = [False]
        self.assertEqual(ratio.getRatio(testLst), 0)

if __name__ == '__main__':
    unittest.main()
