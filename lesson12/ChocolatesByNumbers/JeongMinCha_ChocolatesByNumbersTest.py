"""
Created by JeongMinCha on 2016. 8. 4.
"""
import unittest
import JeongMinCha_ChocolatesByNumbers as ChocolatesByNumbers

class TestChocolatesByNumbers(unittest.TestCase):
    def test_solution(self):
        N = 10; M = 4
        expected = 5
        self.assertEquals(expected, ChocolatesByNumbers.solution(N, M))

if __name__ == '__main__':
    unittest.main()
