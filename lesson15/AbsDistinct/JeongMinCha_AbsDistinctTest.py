"""
Created by JeongMinCha on 2016. 8. 12.
"""
import unittest
from JeongMinCha_AbsDistinct import solution


class TestAbsDistinct(unittest.TestCase):
    def test_solution(self):
        A = [-5, -3, -1, 0, 3, 6]
        expected = 5
        self.assertEqual(expected, solution(A))

if __name__ == '__main__':
    unittest.main()