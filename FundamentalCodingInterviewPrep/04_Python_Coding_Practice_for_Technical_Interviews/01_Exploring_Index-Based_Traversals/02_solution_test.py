import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 0, 2], [2, 0, 1]), [2, 4, 4])

    def test2(self):
        self.assertEqual(solution([0, 0, 0, 0, 0], [0, 0, 1, 2, 3]), [2, 3, 3, 3, 3])

    def test3(self):
        self.assertEqual(solution([1, 2, 3, 0], [2, 3, 0, 1]), [8, 8, 8, 8])

    def test4(self):
        self.assertEqual(solution([2, 2, 2, 2], [3, 2, 1, 0]), [3, 2, 3, 3])

    def test5(self):
        self.assertEqual(solution([1, 2, 1], [0, 2, 1]), [3, 2, 2])

if __name__ == '__main__':
    unittest.main()