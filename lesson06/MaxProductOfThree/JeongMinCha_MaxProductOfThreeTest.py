"""
Created by JeongMinCha on 2016. 7. 27.
"""
import unittest
import JeongMinCha_MaxProductOfThree as MaxProductOfThree

class TestMaxProductOfThree(unittest.TestCase):
    def test_solution(self):
        A = [-3, 1, 2, -2, 5, 6]
        expected = 60
        self.assertEqual(expected, MaxProductOfThree.solution(A))

if __name__ == '__main__':
    unittest.main()