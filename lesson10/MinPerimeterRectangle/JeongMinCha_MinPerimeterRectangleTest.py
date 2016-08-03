"""
Created by JeongMinCha on 2016. 8. 3.
"""
import unittest
import JeongMinCha_MinPerimeterRectangle as MinPerimeterRectangle

class TestCountFactors(unittest.TestCase):
    def test_solution(self):
        N = 30
        expected = 22
        self.assertEquals(expected, MinPerimeterRectangle.solution(N))

if __name__ == '__main__':
    unittest.main()
