"""
Created by JeongMinCha on 2016. 8. 3.
"""
import unittest
import JeongMinCha_CountFactors as CountFactors

class TestCountFactors(unittest.TestCase):
    def test_solution(self):
        N = 24
        expected = 8
        self.assertEquals(expected, CountFactors.solution(N))

if __name__ == '__main__':
    unittest.main()
