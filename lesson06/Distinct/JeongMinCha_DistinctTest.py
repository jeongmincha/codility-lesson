"""
Created by JeongMinCha on 2016. 7. 27.
"""
import unittest
import JeongMinCha_Distinct as Distinct

class TestDistinct(unittest.TestCase):
    def test_solution(self):
        A = [2, 1, 1, 2, 3, 1]
        expected = 3
        self.assertEqual(expected, Distinct.solution(A))

if __name__ == '__main__':
    unittest.main()