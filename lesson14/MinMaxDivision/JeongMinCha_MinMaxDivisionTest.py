"""
Created by JeongMinCha on 2016. 8. 10.
"""
import unittest
from JeongMinCha_MinMaxDivision import solution


class TestMinMaxDivision(unittest.TestCase):
    def test_solution(self):
        K = 3
        M = 5
        A = [2, 1, 5, 1, 2, 2, 2]
        expected = 6
        self.assertEqual(expected, solution(K, M, A))

if __name__ == '__main__':
    unittest.main()