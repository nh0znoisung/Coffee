import unittest
from CoffeeSystem import CoffeeSystem

class TestStringMethods(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    def test_1(self):
        self.assertEqual(division(4, 2), 2)

    # def test_2(self):
    #     self.assertEqual(division(4, 0), "Error")

    def test_3(self):
        self.assertEqual(division(4, 1), 4)

if __name__ == '__main__':
    unittest.main()