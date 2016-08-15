"""
Created by JeongMinCha on 2016. 8. 15.
"""
import unittest
from JeongMinCha_MinAbsSumOfTwo import solution


class TestMinAbsSumOfTwo(unittest.TestCase):
    def test_solution(self):
        A = [-8, 4, 5, -10, 3]
        expected = 3
        self.assertEqual(expected, solution(A))

    def test_short_problem(self):
        A = [1, 4, -3]
        expected = 1
        self.assertEqual(expected, solution(A))


if __name__ == '__main__':
    # print ("Hello World")
    unittest.main()
