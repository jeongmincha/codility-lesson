"""
Created by JeongMinCha on 2016. 7. 29.
"""
import unittest
import JeongMinCha_Dominator as Dominator

class TestDominator(unittest.TestCase):
    def test_solution(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        expected = [0, 2, 4, 6, 7]
        assert Dominator.solution(A) in expected

if __name__ == '__main__':
    unittest.main()