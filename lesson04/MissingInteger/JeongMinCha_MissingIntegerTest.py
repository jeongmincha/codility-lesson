"""
Created by JeongMinCha on 2016. 7. 21.
"""
import unittest
import JeongMinCha_MissingInteger

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        expected = 5
        actual = JeongMinCha_MissingInteger.solution([1, 3, 6, 4, 1, 2])
        self.assertEqual(expected, actual)

    def test_single_element(self):
        expected = 2
        actual = JeongMinCha_MissingInteger.solution([1])
        self.assertEqual(expected, actual)

    def test_minus_element(self):
        expected = 6
        actual = JeongMinCha_MissingInteger.solution([1, 2, -4, -5, 3, 4, 5, 7])
        self.assertEqual(expected, actual)

    def test_permutation(self):
        expected = 501
        actual = JeongMinCha_MissingInteger.solution([x for x in range(1, 501)])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()