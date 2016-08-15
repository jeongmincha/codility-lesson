"""
Created by JeongMinCha on 2016. 8. 15.
"""
import unittest
from JeongMinCha_MaxNonoverlappingSegments import solution


class TestMaxNonoverlappingSegments(unittest.TestCase):
    def test_solution(self):
        A = [1, 3, 7, 9, 9]
        B = [5, 6, 8, 9, 10]
        expected = 3
        self.assertEqual(expected, solution(A, B))

if __name__ == '__main__':
    unittest.main()