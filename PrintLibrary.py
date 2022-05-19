from termcolor import colored, cprint

COFFEE_LENGTH_FRAME = 93 
COFFEE_NUMBER_OF_COLUMN = 3
COFFEE_LENGTH_COLUMN = COFFEE_LENGTH_FRAME//COFFEE_NUMBER_OF_COLUMN
COFFEE_WELCOME = "Welcome to CodeWithMe's coffee"
COFFEE_LENGTH_IDX = 4
COFFEE_LENGTH_QUANTITY = 11
COFFEE_LENGTH_NAME = COFFEE_LENGTH_COLUMN-COFFEE_LENGTH_IDX-COFFEE_LENGTH_QUANTITY

TOPPING_LENGTH_FRAME = 120
TOPPING_NUMBER_OF_COLUMN = 4
TOPPING_WELCOME = "Welcome to CodeWithMe's topping"
TOPPING_LENGTH_COLUMN = TOPPING_LENGTH_FRAME//TOPPING_NUMBER_OF_COLUMN
TOPPING_LENGTH_IDX = 4
TOPPING_LENGTH_QUANTITY = 11
TOPPING_LENGTH_NAME = TOPPING_LENGTH_COLUMN-TOPPING_LENGTH_IDX-TOPPING_LENGTH_QUANTITY

CART_LENGTH_FRAME = 90
CART_WELCOME = "This is your order"
CART_INDENT_COFFEE = 15
CART_INDENT_TOPPING = 30

def printTextRepeat(txt: str, size: int, color: str = "white"):
    print(colored(txt*size, color))

def printTextAlignCenter(txt: str, size: int, color: str = "white"):
    left_space = int((size-len(txt))/2)
    right_space = size-len(txt)-left_space
    cprint(" "*left_space+ txt + " "*right_space, color, end='')

def printTextAlignLeft(txt: str, size: int, color: str = "white"):
    right_space = size-len(txt)
    cprint(txt+" "*right_space, color, end='')

def printTextAlignRight(txt: str, size: int, color: str = "white"):
    left_space = size-len(txt)
    cprint(" "*left_space + txt, color, end='')

def printTextIndent(txt: str, indent: int, color: str = "white"):
    cprint(" "*indent + txt, color, end='\n')
