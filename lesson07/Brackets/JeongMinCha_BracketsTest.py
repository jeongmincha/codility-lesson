"""
Created by JeongMinCha on 2016. 7. 29.
"""
import unittest
import JeongMinCha_Brackets as Brackets

class TestBrackets(unittest.TestCase):
    def test_positive_solution(self):
        S = "{[()()]}"
        expected = 1
        self.assertEqual(expected, Brackets.solution(S))

    def test_negative_solution(self):
        S = "([)()]"
        expected = 0
        self.assertEqual(expected, Brackets.solution(S))

if __name__ == '__main__':
    unittest.main()