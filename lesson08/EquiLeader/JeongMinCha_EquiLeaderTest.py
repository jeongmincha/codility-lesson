"""
Created by JeongMinCha on 2016. 7. 29.
"""
import unittest
import JeongMinCha_EquiLeader as EquiLeader

class TestEquiLeader(unittest.TestCase):
    def test_solution(self):
        A = [4, 3, 4, 4, 4, 2]
        expected = 2
        self.assertEqual(expected, EquiLeader.solution(A))

if __name__ == '__main__':
    unittest.main()