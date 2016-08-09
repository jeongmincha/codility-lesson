"""
Created by JeongMinCha on 2016. 8. 4.
"""
import unittest
import JeongMinCha_FibFrog as FibFrog


class TestFibFrog(unittest.TestCase):
    def test_solution(self):
        A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        expected = 3
        self.assertEquals(expected, FibFrog.solution(A))

if __name__ == '__main__':
    unittest.main()
