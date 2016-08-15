"""
Created by JeongMinCha on 2016. 8. 12.
"""
import unittest
from JeongMinCha_CountTriangles import solution


class TestCountTriangles(unittest.TestCase):
    def test_solution(self):
        A = [10, 2, 5, 1, 8, 12]
        expected = 4
        self.assertEqual(expected, solution(A))

if __name__ == '__main__':
    unittest.main()