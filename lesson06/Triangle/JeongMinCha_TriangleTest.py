"""
Created by JeongMinCha on 2016. 7. 27.
"""
import unittest
import JeongMinCha_Triangle as Triangle

class TestMaxProductOfThree(unittest.TestCase):
    def test_positive_example(self):
        A = [10, 2, 5, 1, 8, 20]
        expected = 1
        self.assertEqual(expected, Triangle.solution(A))

    def test_negative_example(self):
        A = [10, 50, 5, 1]
        expected = 0
        self.assertEqual(expected, Triangle.solution(A))

if __name__ == '__main__':
    unittest.main()