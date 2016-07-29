"""
Created by JeongMinCha on 2016. 7. 30.
"""
import unittest
import JeongMinCha_MaxSliceSum as MaxSliceSum

class TestMaxSliceSum(unittest.TestCase):
    def test_solution(self):
        A = [3, 2, -6, 4, 0]
        expected = 5
        self.assertEquals(expected, MaxSliceSum.solution(A))

if __name__ == '__main__':
    unittest.main()
