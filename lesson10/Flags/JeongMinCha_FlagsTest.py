"""
Created by JeongMinCha on 2016. 8. 3.
"""
import unittest
import JeongMinCha_Flags as Flags

class TestFlags(unittest.TestCase):
    def test_solution(self):
        A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        expected = 3
        self.assertEquals(expected, Flags.solution(A))

if __name__ == '__main__':
    unittest.main()
