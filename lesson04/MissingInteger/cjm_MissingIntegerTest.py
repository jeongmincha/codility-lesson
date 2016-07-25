import unittest
import cjm_MissingInteger

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        expected = 5
        actual = cjm_MissingInteger.solution([1, 3, 6, 4, 1, 2])
        self.assertEqual(expected, actual)

    def test_single_element(self):
        expected = 2
        actual = cjm_MissingInteger.solution([1])
        self.assertEqual(expected, actual)

    def test_minus_element(self):
        expected = 6
        actual = cjm_MissingInteger.solution([1, 2, -4, -5, 3, 4, 5, 7])
        self.assertEqual(expected, actual)

    def test_permutation(self):
        expected = 501
        actual = cjm_MissingInteger.solution([x for x in range(1, 501)])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()