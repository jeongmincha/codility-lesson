"""
Created by JeongMinCha on 2016. 7. 30.
"""
import unittest
import JeongMinCha_MaxProfit as MaxProfit

class TestMaxDoubleSliceSum(unittest.TestCase):
    def test_solution(self):
        A = [23171, 21011, 21123, 21366, 21013, 21367]
        expected = 356
        self.assertEquals(expected, MaxProfit.solution(A))

if __name__ == '__main__':
    unittest.main()
