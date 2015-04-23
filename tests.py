import unittest
import ratio

class MyTest(unittest.TestCase):

    # Test normal bounds of ratio
    def test_ratioNorm1(self):
        testLst = "N" * 300 + "A" * 300
        self.assertEqual(ratio.getRatio(testLst), 1)

    def test_ratioNorm2(self):
        testLst = "A" * 300 + "N" * 300
        self.assertEqual(ratio.getRatio(testLst), 1)

    def test_ratioNorm3(self):
        testLst = "ANN" * 300
        self.assertEqual(ratio.getRatio(testLst), 0.5)

    # Test 0 edge cases
    def test_ratioZeroDen(self):
        testLst = "A"
        self.assertEqual(ratio.getRatio(testLst), -1)

    def test_ratioZeroNum(self):
        testLst = "N"
        self.assertEqual(ratio.getRatio(testLst), 0)

if __name__ == '__main__':
    unittest.main()
