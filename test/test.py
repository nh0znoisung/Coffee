import unittest, sys

sys.path.append('../src/')

TESTCASE_DIR = "Testcases/"

from main import CoffeeSystem, InvalidInput, OutOfRange


def getCoffeeSystem(file_idx: int):
    new_coffee_system = CoffeeSystem(TESTCASE_DIR + str(file_idx) + '.txt')
    return new_coffee_system.run()



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
        with self.assertRaises(InvalidInput):
            getCoffeeSystem(108)
    
    # If choose more topping
    def test_topping_entry_string(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(109)

    def test_topping_entry_word(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(110)
    def test_topping_entry_special_char(self):
        with self.assertRaises(ValueError):
            getCoffeeSystem(111)

    def test_topping_entry_number(self):
        with self.assertRaises(OutOfRange):
            getCoffeeSystem(112)


class TestCoffeeSystem(unittest.TestCase):
    def test_coffee_system_basic_1(self):
        # 1 coffee, 1 topping
        (rem_data, cart, total_price) = getCoffeeSystem(200)
        rem_data_true = {'coffee': [{'id': 1, 'name': 'Flat white', 'quantity': 117, 'price': 10}, {'id': 2, 'name': 'Americano', 'quantity': 113, 'price': 15}, {'id': 3, 'name': 'Macchiato', 'quantity': 120, 'price': 15}, {'id': 4, 'name': 'Con Panna', 'quantity': 62, 'price': 10}, {'id': 5, 'name': 'Mocha', 'quantity': 18, 'price': 20}, {'id': 6, 'name': 'Caramel Macchiato', 'quantity': 68, 'price': 30}, {'id': 7, 'name': 'Cappuccino', 'quantity': 67, 'price': 25}], 'topping': [{'id': 1, 'name': 'Cinnamon', 'quantity': 76, 'price': 2}, {'id': 2, 'name': 'Whipped Cream', 'quantity': 80, 'price': 4}, {'id': 3, 'name': 'Butter', 'quantity': 46, 'price': 3}, {'id': 4, 'name': 'Cardamom', 'quantity': 106, 'price': 4}, {'id': 5, 'name': 'Peanut Butter', 'quantity': 79, 'price': 5}, {'id': 6, 'name': 'Sprinkles', 'quantity': 46, 'price': 1}, {'id': 7, 'name': 'Cocoa Powder', 'quantity': 58, 'price': 1}, {'id': 8, 'name': 'Chocolate Chips', 'quantity': 92, 'price': 2}, {'id': 9, 'name': 'Honey', 'quantity': 115, 'price': 4}, {'id': 10, 'name': 'Brown Sugar', 'quantity': 80, 'price': 1}, {'id': 11, 'name': 'Molasses', 'quantity': 76, 'price': 5}]} 
        cart_true = [{'id': 1, 'name': 'Flat white', 'quantity': 2, 'price': 10, 'topping': [{'id': 1, 'name': 'Cinnamon', 'quantity': 3, 'price': 2}]}] 
        total_price_true = 32
        self.assertDictEqual(rem_data, rem_data_true)
        self.assertListEqual(cart, cart_true)
        self.assertEqual(total_price, total_price_true) 

    def test_coffee_system_basic_2(self): 
        # 1 coffee, many topping
        (rem_data, cart, total_price) = getCoffeeSystem(201)
        rem_data_true = {'coffee': [{'id': 1, 'name': 'Flat white', 'quantity': 119, 'price': 10}, {'id': 2, 'name': 'Americano', 'quantity': 113, 'price': 15}, {'id': 3, 'name': 'Macchiato', 'quantity': 120, 'price': 15}, {'id': 4, 'name': 'Con Panna', 'quantity': 62, 'price': 10}, {'id': 5, 'name': 'Mocha', 'quantity': 18, 'price': 20}, {'id': 6, 'name': 'Caramel Macchiato', 'quantity': 68, 'price': 30}, {'id': 7, 'name': 'Cappuccino', 'quantity': 0, 'price': 25}], 'topping': [{'id': 1, 'name': 'Cinnamon', 'quantity': 82, 'price': 2}, {'id': 2, 'name': 'Whipped Cream', 'quantity': 80, 'price': 4}, {'id': 3, 'name': 'Butter', 'quantity': 46, 'price': 3}, {'id': 4, 'name': 'Cardamom', 'quantity': 39, 'price': 4}, {'id': 5, 'name': 'Peanut Butter', 'quantity': 12, 'price': 5}, {'id': 6, 'name': 'Sprinkles', 'quantity': 46, 'price': 1}, {'id': 7, 'name': 'Cocoa Powder', 'quantity': 58, 'price': 1}, {'id': 8, 'name': 'Chocolate Chips', 'quantity': 92, 'price': 2}, {'id': 9, 'name': 'Honey', 'quantity': 115, 'price': 4}, {'id': 10, 'name': 'Brown Sugar', 'quantity': 80, 'price': 1}, {'id': 11, 'name': 'Molasses', 'quantity': 9, 'price': 5}]} 
        cart_true = [{'id': 7, 'name': 'Cappuccino', 'quantity': 67, 'price': 25, 'topping': [{'id': 11, 'name': 'Molasses', 'quantity': 1, 'price': 5}, {'id': 4, 'name': 'Cardamom', 'quantity': 1, 'price': 4}, {'id': 5, 'name': 'Peanut Butter', 'quantity': 1, 'price': 5}]}] 
        total_price_true = 2613
        self.assertDictEqual(rem_data, rem_data_true)
        self.assertListEqual(cart, cart_true)
        self.assertEqual(total_price, total_price_true) 

    def test_coffee_system_complex_1(self):
        # many coffee, many topping
        (rem_data, cart, total_price) = getCoffeeSystem(202)
        rem_data_true = {'coffee': [{'id': 1, 'name': 'Flat white', 'quantity': 99, 'price': 10}, {'id': 2, 'name': 'Americano', 'quantity': 113, 'price': 15}, {'id': 3, 'name': 'Macchiato', 'quantity': 108, 'price': 15}, {'id': 4, 'name': 'Con Panna', 'quantity': 62, 'price': 10}, {'id': 5, 'name': 'Mocha', 'quantity': 18, 'price': 20}, {'id': 6, 'name': 'Caramel Macchiato', 'quantity': 68, 'price': 30}, {'id': 7, 'name': 'Cappuccino', 'quantity': 67, 'price': 25}], 'topping': [{'id': 1, 'name': 'Cinnamon', 'quantity': 82, 'price': 2}, {'id': 2, 'name': 'Whipped Cream', 'quantity': 80, 'price': 4}, {'id': 3, 'name': 'Butter', 'quantity': 10, 'price': 3}, {'id': 4, 'name': 'Cardamom', 'quantity': 106, 'price': 4}, {'id': 5, 'name': 'Peanut Butter', 'quantity': 79, 'price': 5}, {'id': 6, 'name': 'Sprinkles', 'quantity': 46, 'price': 1}, {'id': 7, 'name': 'Cocoa Powder', 'quantity': 58, 'price': 1}, {'id': 8, 'name': 'Chocolate Chips', 'quantity': 92, 'price': 2}, {'id': 9, 'name': 'Honey', 'quantity': 15, 'price': 4}, {'id': 10, 'name': 'Brown Sugar', 'quantity': 20, 'price': 1}, {'id': 11, 'name': 'Molasses', 'quantity': 76, 'price': 5}]} 
        cart_true = [{'id': 3, 'name': 'Macchiato', 'quantity': 12, 'price': 15, 'topping': [{'id': 10, 'name': 'Brown Sugar', 'quantity': 5, 'price': 1}, {'id': 3, 'name': 'Butter', 'quantity': 3, 'price': 3}]}, {'id': 1, 'name': 'Flat white', 'quantity': 20, 'price': 10, 'topping': [{'id': 9, 'name': 'Honey', 'quantity': 5, 'price': 4}]}] 
        total_price_true = 948
        self.assertDictEqual(rem_data, rem_data_true)
        self.assertListEqual(cart, cart_true)
        self.assertEqual(total_price, total_price_true) 
    
    def test_coffee_system_complex_2(self):
        # many coffee, many topping
        (rem_data, cart, total_price) = getCoffeeSystem(203)
        rem_data_true = {'coffee': [{'id': 1, 'name': 'Flat white', 'quantity': 99, 'price': 10}, {'id': 2, 'name': 'Americano', 'quantity': 113, 'price': 15}, {'id': 3, 'name': 'Macchiato', 'quantity': 108, 'price': 15}, {'id': 4, 'name': 'Con Panna', 'quantity': 62, 'price': 10}, {'id': 5, 'name': 'Mocha', 'quantity': 18, 'price': 20}, {'id': 6, 'name': 'Caramel Macchiato', 'quantity': 0, 'price': 30}, {'id': 7, 'name': 'Cappuccino', 'quantity': 67, 'price': 25}], 'topping': [{'id': 1, 'name': 'Cinnamon', 'quantity': 82, 'price': 2}, {'id': 2, 'name': 'Whipped Cream', 'quantity': 80, 'price': 4}, {'id': 3, 'name': 'Butter', 'quantity': 10, 'price': 3}, {'id': 4, 'name': 'Cardamom', 'quantity': 106, 'price': 4}, {'id': 5, 'name': 'Peanut Butter', 'quantity': 79, 'price': 5}, {'id': 6, 'name': 'Sprinkles', 'quantity': 46, 'price': 1}, {'id': 7, 'name': 'Cocoa Powder', 'quantity': 58, 'price': 1}, {'id': 8, 'name': 'Chocolate Chips', 'quantity': 92, 'price': 2}, {'id': 9, 'name': 'Honey', 'quantity': 15, 'price': 4}, {'id': 10, 'name': 'Brown Sugar', 'quantity': 20, 'price': 1}, {'id': 11, 'name': 'Molasses', 'quantity': 8, 'price': 5}]} 
        cart_true = [{'id': 3, 'name': 'Macchiato', 'quantity': 12, 'price': 15, 'topping': [{'id': 10, 'name': 'Brown Sugar', 'quantity': 5, 'price': 1}, {'id': 3, 'name': 'Butter', 'quantity': 3, 'price': 3}]}, {'id': 1, 'name': 'Flat white', 'quantity': 20, 'price': 10, 'topping': [{'id': 9, 'name': 'Honey', 'quantity': 5, 'price': 4}]}, {'id': 6, 'name': 'Caramel Macchiato', 'quantity': 68, 'price': 30, 'topping': [{'id': 11, 'name': 'Molasses', 'quantity': 1, 'price': 5}]}] 
        total_price_true = 3328
        self.assertDictEqual(rem_data, rem_data_true)
        self.assertListEqual(cart, cart_true)
        self.assertEqual(total_price, total_price_true) 



if __name__ == '__main__':
    unittest.main()

