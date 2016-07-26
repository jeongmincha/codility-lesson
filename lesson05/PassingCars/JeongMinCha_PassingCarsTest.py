"""
Created by JeongMinCha on 2016. 7. 26.
"""
import unittest
import JeongMinCha_PassingCars as PassingCars

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        A = [0,1,0,1,1]
        expected = 5
        self.assertEqual(expected, PassingCars.solution(A))

if __name__ == '__main__':
    unittest.main()