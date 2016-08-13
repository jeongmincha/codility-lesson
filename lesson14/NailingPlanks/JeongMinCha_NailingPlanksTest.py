"""
Created by JeongMinCha on 2016. 8. 10.
"""
import unittest
from JeongMinCha_NailingPlanks import solution


class TestNailingPlanks(unittest.TestCase):
    def test_solution(self):
        A = [1, 4, 5, 8]
        B = [4, 5, 9, 10]
        C = [4, 6, 7, 10, 2]
        expected = 4
        self.assertEqual(expected, solution(A, B, C))

if __name__ == '__main__':
    unittest.main()