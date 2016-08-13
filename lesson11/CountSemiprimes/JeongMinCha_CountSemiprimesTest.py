"""
Created by JeongMinCha on 2016. 8. 4.
"""
import unittest
import JeongMinCha_CountSemiprimes as CountSemiprimes

class TestCountSemiprimes(unittest.TestCase):
    def test_solution(self):
        N = 26
        P = [1, 4, 16]
        Q = [26, 10, 20]
        expected = [10, 4, 0]
        self.assertEquals(expected, CountSemiprimes.solution(N, P, Q))

if __name__ == '__main__':
    unittest.main()
