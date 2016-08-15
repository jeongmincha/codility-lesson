"""
Created by JeongMinCha on 2016. 8. 16.
"""
import unittest
from JeongMinCha_NumberSolitaire import solution


class TestNumberSolitaire(unittest.TestCase):
    def test_solution(self):
        A = [1, -2, 0, 9, -1, -2]
        expected = 8
        self.assertEqual(expected, solution(A))

if __name__ == '__main__':
    unittest.main()
