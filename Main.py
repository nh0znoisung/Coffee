from termcolor import colored, cprint
from GetData import getData
import StatusVisitor
from ExportFactory import *
from ExportStrategy import *
from BillExport import BillExport
from PrintLibrary import *
from GetData import *
from PrintProductVisitor import *


data = getData(FILE_DATA)
cart = [] 

def getCoffeeInput() -> int:
    while True:
        low, high = 1, len(data['coffee'])
        coffee_id = input(colored('Please choose your coffee! [{}-{}]:  '.format(low,high), 'blue', attrs=['blink']))
        if checkRangeInteger(coffee_id, low, high):
            return int(coffee_id)
        cprint("Your input is not valid! Please try again", 'red')

def getCoffeeQuantity(low: int, high: int) -> int:
    while True:
        coffee_quantity = int(input(colored('How many coffee do you want? ', 'blue', attrs=['blink'])))
        if checkRangeInteger(coffee_quantity, low, high):
            return int(coffee_quantity)
        elif int(coffee_quantity) < low or int(coffee_quantity) > high:
            raise ValueError('Out of range!')
        cprint("Your input is not valid! Please try again", 'red')

def getCoffeeById(id: str) -> dict:
    for coffee in data['coffee']:
        if coffee['id'] == id:
            return coffee.copy()
    return None

def getToppingInput() -> int:
    while True:
        low, high = 1, len(data['topping'])
        topping_id = input(colored('Please choose your topping! [{}-{}]:  '.format(low,high), 'blue', attrs=['blink']))
        if checkRangeInteger(topping_id, low, high):
            return int(topping_id)
        cprint("Your input is not valid! Please try again", 'red')

def getToppingById(coffee, topping_id) -> dict:
    # If already have in coffee's topping, just return the actual one
    # Else return a copy of new_topping
    for topping in coffee['topping']:
        if topping['id'] == topping_id:
            return topping, False
    for topping in data['topping']:
        if topping['id'] == topping_id:
            return topping.copy(), True
    return None

def getToppingQuantity(low: int, high: int, coffee_quantity: int) -> int:
    while True:
        topping_quantity = int(input(colored('How many topping do you want? ', 'blue', attrs=['blink'])))
        if checkRangeInteger(topping_quantity*coffee_quantity , low, high):
            return int(topping_quantity)
        elif int(topping_quantity)*coffee_quantity < low or int(topping_quantity)*coffee_quantity > high:
            raise ValueError('Out of range!')
        cprint("Your input is not valid! Please try again", 'red')

def isToppingContinue():
    while True:
        is_topping_continue = input(colored('Do you want to add topping? [Y/N]: ', 'blue', attrs=['blink']))
        if is_topping_continue.upper() == 'Y':
            return True
        elif is_topping_continue.upper() == 'N':
            return False
        else:
            cprint("Your input is not valid! Please try again", 'red')

def isCoffeeContinue():
    while True:
        is_coffee_continue = input(colored('Do you want to choose more coffee? [Y/N]: ', 'blue', attrs=['blink']))
        if is_coffee_continue.upper() == 'Y':
            return True
        elif is_coffee_continue.upper() == 'N':
            return False
        else:
            cprint("Your input is not valid! Please try again", 'red')

def calcCartTotal(cart: list) -> float:
    total_price = 0
    for coffee in cart:
        total_topping = 0
        for topping in coffee['topping']:
            total_topping += topping['price'] * topping['quantity']
        total_price += (coffee['price'] + total_topping) * coffee['quantity'] 

    return total_price

def getPhoneNumber():
    while True:
        phone_number = input(colored('Please enter your phone number: ', 'blue', attrs=['blink']))
        if phone_number.isdigit():
            return phone_number
        cprint("Your input is not valid! Please try again", 'red')

### Send Staus Order
def isSendStatusOrder():
    while True:
        is_send_status = input(colored('Do you want to send status order? [Y/N]: ', 'blue', attrs=['blink']))
        if is_send_status.upper() == 'Y':
            return True
        elif is_send_status.upper() == 'N':
            return False
        else:
            cprint("Your input is not valid! Please try again", 'red')

def chooseMethodExportStatus():
    while True:
        method_export = input(colored('Please choose method send (Telegram/Zalo/Messenger) [T/Z/M]: ', 'blue', attrs=['blink']))
        if method_export.upper() not in ['T','Z','M']:
            cprint("Your input is not valid! Please try again", 'red')
        else:
            chatapp_instance, chatapp_strategy = None, None
            if method_export.upper() in ['T','Z']:
                phone_number = getPhoneNumber()
                if method_export.upper() == 'T':
                    chatapp_instance = TelegramFactory.getInstance()
                else:
                    chatapp_instance = ZaloFactory.getInstance()
                chatapp_strategy = chatapp_instance.createStrategy(phone_number) 
            elif method_export.upper() == 'M':
                id = input(colored('Please enter your id: ', 'blue', attrs=['blink']))
                chatapp_instance = MessengerFactory.getInstance()
                chatapp_strategy = chatapp_instance.createStrategy(id) 
            
            StatusVisitor.cas = chatapp_strategy # Set strategy
            return
            
    

## Print bill
def isPrintBill():
    while True:
        is_print_bill = input(colored('Do you want to print bill? [Y/N]: ', 'blue', attrs=['blink']))
        if is_print_bill.upper() == 'Y':
            return True
        elif is_print_bill.upper() == 'N':
            return False
        else:
            cprint("Your input is not valid! Please try again", 'red')

def chooseMethodPrint():
    while True:
        method_print = input(colored('Please choose method print (Printer/Telegram/Zalo/Messenger) [P/T/Z/M]: ', 'blue', attrs=['blink']))
        if method_print.upper() not in ['P','T','Z','M']:
            cprint("Your input is not valid! Please try again", 'red')
        else:
            export_instance, export_strategy = None, None
            if method_print.upper() == 'P':
                export_instance = PrinterFactory.getInstance()
                export_strategy = export_instance.createStrategy() 
            elif method_print.upper() in ['T','Z']:
                phone_number = getPhoneNumber()
                if method_print.upper() == 'T':
                    export_instance = TelegramFactory.getInstance()
                else:
                    export_instance = ZaloFactory.getInstance()
                export_strategy = export_instance.createStrategy(phone_number) 
            elif method_print.upper() == 'M':
                id = input(colored('Please enter your id: ', 'blue', attrs=['blink']))
                export_instance = MessengerFactory.getInstance()
                export_strategy = export_instance.createStrategy(id) 

            BillExport.print_bill(export_strategy)
            return



def main():
    global data, cart
    # while true
    while True:
        PrintCoffee(data['coffee']).accept(PrintMenu())

        coffee_id = getCoffeeInput()
        new_coffee = getCoffeeById(coffee_id)

        coffee_quantity = getCoffeeQuantity(1,new_coffee['quantity'])

        new_coffee['quantity'] = coffee_quantity
        for coffee in data['coffee']:
            if coffee['id'] == coffee_id:
                coffee['quantity'] -= coffee_quantity

        new_coffee['topping'] = []
        while True:
            is_topping_continue = isToppingContinue()
            if is_topping_continue == False:
                break

            PrintTopping(data['topping']).accept(PrintMenu())

            topping_id = getToppingInput()
            new_topping, is_new = getToppingById(new_coffee, topping_id)

            topping_quantity = getToppingQuantity(1, new_topping['quantity'], coffee_quantity)

            new_topping['quantity'] = topping_quantity
            for topping in data['topping']:
                if topping['id'] == topping_id:
                    topping['quantity'] -= topping_quantity * coffee_quantity
            
            if is_new: 
                new_coffee['topping'].append(new_topping)

        cart.append(new_coffee)
        
        is_coffee_continue = isCoffeeContinue()
        if is_coffee_continue == False:
            break
    
    total_price = calcCartTotal(cart)

    PrintCart(cart, total_price).accept(PrintMenu())

    StatusVisitor.sendStatus() # Timer starts here
    is_send_status = isSendStatusOrder()
    if is_send_status:
        StatusVisitor.is_disable = False
        chooseMethodExportStatus()
    else:
        StatusVisitor.cancelStatus()
    
    is_print_bill = isPrintBill()
    if is_print_bill:
        chooseMethodPrint()
    

    return data, cart, total_price
    


main()
