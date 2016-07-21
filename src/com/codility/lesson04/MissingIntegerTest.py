import unittest
import MissingInteger

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        expected = 5
        actual = MissingInteger.solution([1, 3, 6, 4, 1, 2])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()