from dataclasses import dataclass
from PrintLibrary import *
from GetData import *

class Print:
    def accept(self, visitor):
        return visitor.visit(self)

@dataclass
class PrintCoffee(Print):
    data: list = None
    length_frame: int = COFFEE_LENGTH_FRAME
    length_idx: int = COFFEE_LENGTH_IDX
    length_name: int = COFFEE_LENGTH_NAME
    length_quantity: int = COFFEE_LENGTH_QUANTITY
    number_of_column: int = COFFEE_NUMBER_OF_COLUMN
    welcome: str = COFFEE_WELCOME

@dataclass
class PrintTopping(Print):
    data: list = None    
    length_frame: int = TOPPING_LENGTH_FRAME
    length_idx: int = TOPPING_LENGTH_IDX
    length_name: int = TOPPING_LENGTH_NAME
    length_quantity: int = TOPPING_LENGTH_QUANTITY
    number_of_column: int = TOPPING_NUMBER_OF_COLUMN
    welcome: str = TOPPING_WELCOME

@dataclass
class PrintCart(Print):
    cart: list = None
    total_price: int = None
    welcome: str = CART_WELCOME
    indent_coffee: int = CART_INDENT_COFFEE
    indent_topping: int = CART_INDENT_TOPPING
    length_frame: int = CART_LENGTH_FRAME

class Visitor:
    def visit(self, print: Print): pass

@dataclass
class PrintContent(Visitor):
    def visit(self, prt: Print):
        if type(prt) is PrintCart:
            for coffee in prt.cart:
                id, name, quantity, price, topping_list = coffee['id'], coffee['name'], coffee['quantity'], coffee['price'], coffee['topping']
                printTextIndent('- ID: '+ str(id), prt.indent_coffee-2, "green")
                printTextIndent('Name: '+name, prt.indent_coffee, "green")
                printTextIndent('Quantity: '+str(quantity), prt.indent_coffee, "green")
                printTextIndent('Price: '+str(price), prt.indent_coffee, "green")
                
                for topping in topping_list:
                    printTextIndent('+ ID: '+ str(topping['id']), prt.indent_topping-2, "yellow")
                    printTextIndent('Name: ' + topping['name'], prt.indent_topping, "yellow")
                    printTextIndent('Quantity: ' + str(topping['quantity']), prt.indent_topping, "yellow")
                    printTextIndent('Price: ' + str(topping['price']), prt.indent_topping, "yellow")

                print()
            printTextAlignCenter("Your total price is: " + str(prt.total_price), prt.length_frame, 'red')
            print()
        else: # PrintCoffee or PrintTopping
            count_idx = 0
            for obj in prt.data:
                count_idx += 1
                (id, name, quantity,_) = obj['id'], obj['name'], obj['quantity'], obj['price'] 
                printTextAlignLeft(str(id)+')', prt.length_idx, "cyan")
                printTextAlignLeft(name, prt.length_name, "cyan")
                printTextAlignCenter(str(quantity), prt.length_quantity, "yellow")

                if count_idx%prt.number_of_column == 0:
                    print()
            if (len(prt.data))%prt.number_of_column != 0:
                print()

@dataclass
class PrintMenu(Visitor):
    def visit(self, prt: Print):
        printTextRepeat("*", prt.length_frame, "cyan")
        printTextAlignCenter(prt.welcome, prt.length_frame, 'magenta')
        print()
        print()
        prt.accept(PrintContent())
        printTextRepeat("*", prt.length_frame, "cyan")

