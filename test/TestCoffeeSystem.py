import unittest, sys

sys.path.append('../src/')

TESTCASE_DIR = "Testcases/"

from CoffeeSystem import CoffeeSystem, InvalidInput, OutOfRange, NoItem


def getCoffeeSystem(file_idx: int):
    return CoffeeSystem(TESTCASE_DIR + str(file_idx) + '.txt').run()

# At lease 1 type of error
class TestSyntax(unittest.TestCase): 
    # Check coffee entry
    def test_coffee_entry_string(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(100)
    
    def test_coffee_entry_word(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(101)
    
    def test_coffee_entry_special_char(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(102)

    # Check input coffee quantity
    def test_coffee_quantity_string(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(103)

    def test_coffee_quantity_word(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(104)

    def test_coffee_quantity_special_char(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(105)
    
    # Check want more topping?
    def test_want_more_topping_string(self):            
        with self.assertRaises(InvalidInput):
            getCoffeeSystem(106)

    def test_want_more_topping_special_char(self):            
        with self.assertRaises(InvalidInput):
            getCoffeeSystem(107)

    def test_want_more_topping_number(self):            
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(108)
    
    # If choose more topping
    def test_topping_entry_string(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(109)

    def test_topping_entry_word(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(110)
    
    def test_topping_entry_special_char(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(111)

    def test_topping_entry_number(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(112)

    # Check out of range
    def test_coffee_quantity_positive(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(113)

    def test_coffee_quantity_negative(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(114)
    
    def test_topping_quantity_positive(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(115)

    def test_topping_quantity_negative(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(116)
    
    # Check no item
    def test_no_item_coffee(self):
        with self.assertRaises(NoItem):
            getCoffeeSystem(117)
    

class TestOutOfRange(unittest.TestCase): pass
class TestTotalPrice(unittest.TestCase): 
    def test_total_price(self):
        (_, _, total_price) = getCoffeeSystem(200)
        self.assertEqual(total_price, 32)


class TestCart(unittest.TestCase): pass
class TestCoffeeRemaining(unittest.TestCase): 
    D1 = {'a': 1, 'b': 2, 'c': [1, 2]}
    D2 = {'a': 1, 'b': 2, 'c': [1, 2]}

    def test_useful(self):
        self.assertDictEqual(self.D1, self.D2)

if __name__ == '__main__':
    unittest.main()

