import unittest
from CoffeeSystem import CoffeeSystem, InvalidInput

TESTCASE_DIR = "Testcases/"

def getCoffeeSystem(file_idx: int):
    return CoffeeSystem(TESTCASE_DIR + str(file_idx) + '.txt').run()



class TestSyntax(unittest.TestCase): 
    def test_true(self):
        with self.assertRaises(InvalidInput):
            getCoffeeSystem(100)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


class TestOutOfRange(unittest.TestCase): pass
class TestTotalPrice(unittest.TestCase): 
    def test_total_price(self):
        (_, _, total_price) = getCoffeeSystem(200)
        self.assertEqual(total_price, 32)


class TestCart(unittest.TestCase): pass
class TestCoffeeRemaining(unittest.TestCase): pass

if __name__ == '__main__':
    unittest.main()

