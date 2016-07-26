"""
Created by JeongMinCha on 2016. 7. 26.
"""
import unittest
import JeongMinCha_MinAvgTwoSlice as MinAvgTwoSlice

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        A = [4, 2, 2, 5, 1, 5, 8]
        expected = 1
        self.assertEqual(expected, MinAvgTwoSlice.solution(A))

if __name__ == '__main__':
    unittest.main()