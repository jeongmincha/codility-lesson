"""
Created by JeongMinCha on 2016. 8. 4.
"""
import unittest
import JeongMinCha_CommonPrimeDivisors as CommonPrimeDivisors

class TestCommonPrimeDivisors(unittest.TestCase):
    def test_solution(self):
        A = [15, 10, 3]
        B = [75, 30, 5]
        expected = 1
        self.assertEquals(expected, CommonPrimeDivisors.solution(A, B))

if __name__ == '__main__':
    unittest.main()
