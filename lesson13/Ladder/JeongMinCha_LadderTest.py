"""
Created by JeongMinCha on 2016. 8. 9.
"""
import unittest
from JeongMinCha_Ladder import solution


class TestFibFrog(unittest.TestCase):
    def test_solution(self):
        A = [4, 4, 5, 5, 1]
        B = [3, 2, 4, 3, 1]
        expected = [5, 1, 8, 0, 1]
        self.assertEquals(expected, solution(A, B))

if __name__ == '__main__':
    unittest.main()
