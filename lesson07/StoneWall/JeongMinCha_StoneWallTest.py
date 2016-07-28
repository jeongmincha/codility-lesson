"""
Created by JeongMinCha on 2016. 7. 29.
"""
import unittest
import JeongMinCha_StoneWall as StoneWall

class TestStoneWall(unittest.TestCase):
    def test_solution(self):
        H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
        expected = 7
        self.assertEqual(expected, StoneWall.solution(H))

if __name__ == '__main__':
    unittest.main()