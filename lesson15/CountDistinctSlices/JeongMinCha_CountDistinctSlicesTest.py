"""
Created by JeongMinCha on 2016. 8. 12.
"""
import unittest
from JeongMinCha_CountDistinctSlices import solution


class TestCountDistinctSlices(unittest.TestCase):
    def test_solution(self):
        M = 6
        A = [3, 4, 5, 5, 2]
        expected = 9
        self.assertEqual(expected, solution(M, A))

if __name__ == '__main__':
    unittest.main()