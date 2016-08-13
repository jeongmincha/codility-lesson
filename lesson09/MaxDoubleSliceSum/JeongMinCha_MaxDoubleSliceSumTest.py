"""
Created by JeongMinCha on 2016. 7. 30.
"""
import unittest
import JeongMinCha_MaxDoubleSliceSum as MaxDoubleSliceSum

class TestMaxDoubleSliceSum(unittest.TestCase):
    def test_solution(self):
        A = [3, 2, 6, -1, 4, 5, -1, 2]
        expected = 17
        self.assertEquals(expected, MaxDoubleSliceSum.solution(A))

if __name__ == '__main__':
    unittest.main()
