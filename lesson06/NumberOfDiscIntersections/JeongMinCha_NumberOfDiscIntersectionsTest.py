"""
Created by JeongMinCha on 2016. 7. 27.
"""
import unittest
import JeongMinCha_NumberOfDiscIntersections as NumberOfDiscIntersections

class TestNumberOfDiscIntersections(unittest.TestCase):
    def test_positive_example(self):
        A = [1, 5, 2, 1, 4, 0]
        expected = 11
        self.assertEqual(expected, NumberOfDiscIntersections.solution(A))

if __name__ == '__main__':
    unittest.main()
