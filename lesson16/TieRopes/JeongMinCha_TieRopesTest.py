"""
Created by JeongMinCha on 2016. 8. 15.
"""
import unittest
from JeongMinCha_TieRopes import solution


class TestTieRopes(unittest.TestCase):
    def test_solution(self):
        K = 4
        A = [1, 2, 3, 4, 1, 1, 3]
        expected = 3
        self.assertEqual(expected, solution(K, A))

if __name__ == '__main__':
    unittest.main()