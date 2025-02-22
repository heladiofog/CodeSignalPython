import unittest
from solution import solution

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('398746', '199234'), '199512')

    def test2(self):
        self.assertEqual(solution('100', '1'), '99')

    def test3(self):
        self.assertEqual(solution('9', '1'), '8')

    def test4(self):
        self.assertEqual(solution('501', '105'), '396')

    def test5(self):
        self.assertEqual(solution('1000', '999'), '1')

    def test6(self):
        self.assertEqual(solution('10000', '1000'), '9000')

    def test7(self):
        self.assertEqual(solution('111111111111111', '111111111111111'), '0')

    def test8(self):
        self.assertEqual(solution('123456789101112131415', '98765432101012131415'), '24691357000100000000')

    def test9(self):
        self.assertEqual(solution('500', '500'), '0')

if __name__ == '__main__':
    unittest.main()