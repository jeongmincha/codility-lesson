"""
Created by JeongMinCha on 2016. 8. 3.
"""
import unittest
import JeongMinCha_Peaks as Peaks

class TestPeaks(unittest.TestCase):
    def test_solution(self):
        A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        expected = 3
        self.assertEquals(expected, Peaks.solution(A))

if __name__ == '__main__':
    unittest.main()
