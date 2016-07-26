"""
Created by JeongMinCha on 2016. 7. 26.
"""
import unittest
import JeongMinCha_CountDiv as CountDiv

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        A = 6; B = 11; K = 2
        expected = 3
        self.assertEqual(expected, CountDiv.solution(A, B, K))

if __name__ == '__main__':
    unittest.main()