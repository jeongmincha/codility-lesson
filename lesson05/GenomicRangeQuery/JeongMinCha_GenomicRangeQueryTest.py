"""
Created by JeongMinCha on 2016. 7. 26.
"""
import unittest
import JeongMinCha_GenomicRangeQuery as GenomicRangeQuery

class TestMissingInteger(unittest.TestCase):
    def test_solution(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        expected = [2, 4, 1]
        self.assertEqual(expected, GenomicRangeQuery.solution(S, P, Q))

if __name__ == '__main__':
    unittest.main()