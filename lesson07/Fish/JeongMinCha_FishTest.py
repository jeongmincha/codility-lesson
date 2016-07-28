"""
Created by JeongMinCha on 2016. 7. 28.
"""
import unittest
import JeongMinCha_Fish as Fish

class TestFish(unittest.TestCase):
    def test_solution(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        expected = 2
        self.assertEqual(expected, Fish.solution(A, B))

if __name__ == '__main__':
    unittest.main()