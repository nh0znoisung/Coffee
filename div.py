

def printCoffeeContent(data):
    for (idx, name, quantity) in data:
        printTextAlignLeft(str(idx)+')', COFFEE_LENGTH_IDX, "cyan")
        printTextAlignLeft(name, COFFEE_LENGTH_NAME, "cyan")
        printTextAlignCenter(str(quantity), COFFEE_LENGTH_QUANTITY, "yellow")

        if (idx)%COFFEE_NUMBER_OF_COLUMN == 0:
            print()
    if (len(data))%COFFEE_NUMBER_OF_COLUMN != 0:
        print()

def printToppingContent(data):
    for (idx, name, quantity) in data:
        printTextAlignLeft(str(idx)+')', TOPPING_LENGTH_IDX, "cyan")
        printTextAlignLeft(name, TOPPING_LENGTH_NAME, "cyan")
        printTextAlignCenter(str(quantity), TOPPING_LENGTH_QUANTITY, "yellow")

        if (idx)%TOPPING_NUMBER_OF_COLUMN == 0:
            print()
    if (len(data)-1)%TOPPING_NUMBER_OF_COLUMN != 0:
        print()
FILE_NAME = "data.json"




data = getData(FILE_NAME)
print(data)
data_coffee = data["coffee"]
data_topping = data["topping"]

printCoffeeMenu(data_coffee)    
# printToppingMenu()


# Show instructions 
# Click Q to quit

def checkRangeInteger(txt: str, low: int, high: int)->bool:
    try:
        num = int(txt)
        if num < low or num > high:
            return False
        return True
    except:
        return False

def getCoffeeInput():
    while True:
        coffee_idx = input(colored('Please choose your coffee! [0-{}]:  '.format(len(data_coffee)-1), 'blue', attrs=['blink']))
        if checkRangeInteger(coffee_idx, 0, len(data_coffee)-1):
            return int(coffee_idx)
        if coffee_idx.upper() == "Q":
            return -1 # Quit the program
        cprint("Your input is not valid! Please try again", 'red')

def getToppingInput():
    while True:
        low = 1
        high = len(data_coffee) - 1
        coffee_idx = input(colored('Please choose your topping! [{}-{}]:  '.format(low, high), 'blue', attrs=['blink']))
        if checkRangeInteger(coffee_idx, 0, len(data_coffee)-1):
            return int(coffee_idx)
        if coffee_idx.upper() == "Q":
            return -1 # Quit the program
        cprint("Your input is not valid! Please try again", 'red')

def printCustomerCart():
    printTextRepeat("*", COFFEE_LENGTH_FRAME, "cyan")
    printTextAlignCenter("Your cart", COFFEE_LENGTH_FRAME, 'magenta')
    print()
    print()
    printTextAlignCenter("Coffee", COFFEE_LENGTH_FRAME, 'cyan')
    printTextAlignCenter("Topping", TOPPING_LENGTH_FRAME, 'cyan')
    printTextRepeat("*", COFFEE_LENGTH_FRAME, "cyan")


