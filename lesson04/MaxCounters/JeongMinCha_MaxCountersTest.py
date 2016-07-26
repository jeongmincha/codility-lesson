"""
Created by JeongMinCha on 2016. 7. 26.
"""
import unittest
import JeongMinCha_MaxCounters

class TestMaxCounters(unittest.TestCase):
    def test_solution(self):
        N = 5
        A = [3,4,4,6,1,4,4]
        expected = [3,2,2,4,2]
        self.assertEqual(expected, JeongMinCha_MaxCounters.solution(N, A))
        return 0

if __name__ == '__main__':
    unittest.main()
