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

    def test_rightmost_peaks(self):
        A = [1, 2, 3, 4, 5, 6, 7, 6, 7, 6, 7, 6]
        expected = 1
        self.assertEquals(expected, Peaks.solution(A))

    def test_leftmost_peaks(self):
        A = [1, 3, 1, 3, 1, 3, 1, 2, 3, 4, 5, 6]
        expected = 1
        self.assertEquals(expected, Peaks.solution(A))

if __name__ == '__main__':
    unittest.main()
