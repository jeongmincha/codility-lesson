"""
Created by JeongMinCha on 2016. 8. 4.
"""
import unittest
import JeongMinCha_CountNonDivisible as CountNonDivisible

class TestCountNonDivisible(unittest.TestCase):
    def test_solution(self):
        A = [3, 1, 2, 3, 6]
        expected = [2, 4, 3, 2, 0]
        self.assertEquals(expected, CountNonDivisible.solution(A))

if __name__ == '__main__':
    unittest.main()
