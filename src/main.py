from termcolor import colored, cprint
from data_preprocessing import getData
import status_visitor
from export_strategy import *
from export_factory import *
from bill_export import BillExport
from print_product_visitor import *
from print_library import *
from contextlib import contextmanager
import sys, os
from error_checker import *


# Silent mode
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

class CoffeeSystem: 
    data = getData(FILE_DATA)
    cart = [] 
    file_mode = False
    file = None

    def __init__(self, filename: str = None):
        status_visitor.is_disable = True
        status_visitor.cas = None
        self.data = getData(FILE_DATA)
        self.cart = []
        if filename is not None:
            self.file_mode = True
            self.file = open(filename, "r")

    def __del__(self):
        if self.file_mode:
            self.file.close()
        self.cart = []
        self.data = None
        self.file_mode = False
        self.file = None

    def getNextLine(self):
        txt = self.file.readline()
        if txt == '':
            exit()
        return txt.strip()


    def getCoffeeInput(self) -> int:
        while True:
            low, high = 1, len(self.data['coffee'])
            coffee_id = input(colored('Please choose your coffee! [{}-{}]:  '.format(low,high), 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if checkRangeInteger(coffee_id, low, high):
                return int(coffee_id)
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def getCoffeeQuantity(self, low: int, high: int) -> int:
        while True:
            coffee_quantity = int(input(colored('How many coffee do you want? ', 'blue', attrs=['blink']))) if self.file_mode == False else self.getNextLine()
            if checkRangeInteger(coffee_quantity, low, high):
                return int(coffee_quantity)
            # elif int(coffee_quantity) < low or int(coffee_quantity) > high:
            #     raise OutOfRange('Your input is out of range!')
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def getCoffeeById(self, id: str) -> dict:
        for coffee in self.data['coffee']:
            if coffee['id'] == id:
                return coffee.copy()
        raise NoItem()

    def getToppingInput(self) -> int:
        while True:
            low, high = 1, len(self.data['topping'])
            topping_id = input(colored('Please choose your topping! [{}-{}]:  '.format(low,high), 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if checkRangeInteger(topping_id, low, high):
                return int(topping_id)
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def getToppingById(self, coffee, topping_id) -> dict:
        # If already have in coffee's topping, just return the actual one
        # Else return a copy of new_topping
        for topping in coffee['topping']:
            if topping['id'] == topping_id:
                return topping, False
        for topping in self.data['topping']:
            if topping['id'] == topping_id:
                return topping.copy(), True
        raise NoItem()

    def getToppingQuantity(self, low: int, high: int, coffee_quantity: int) -> int:
        while True:
            topping_quantity = int(input(colored('How many topping do you want? ', 'blue', attrs=['blink']))) if self.file_mode == False else self.getNextLine()
            if checkRangeInteger(topping_quantity , low/coffee_quantity, high/coffee_quantity):
                return int(topping_quantity)
            # elif int(topping_quantity)*coffee_quantity < low or int(topping_quantity)*coffee_quantity > high:
            #     raise OutOfRange('Your input is out of range!')
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def isToppingContinue(self):
        while True:
            is_topping_continue = input(colored('Do you want to add topping? [Y/N]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if is_topping_continue.upper() == 'Y':
                return True
            elif is_topping_continue.upper() == 'N':
                return False
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def isCoffeeContinue(self):
        while True:
            is_coffee_continue = input(colored('Do you want to choose more coffee? [Y/N]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if is_coffee_continue.upper() == 'Y':
                return True
            elif is_coffee_continue.upper() == 'N':
                return False
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def calcCartTotal(self, cart: list) -> float:
        total_price = 0
        for coffee in cart:
            total_topping = 0
            for topping in coffee['topping']:
                total_topping += topping['price'] * topping['quantity']
            total_price += (coffee['price'] + total_topping) * coffee['quantity'] 

        return total_price

    def getPhoneNumber(self):
        while True:
            phone_number = input(colored('Please enter your phone number: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if phone_number.isdigit():
                return phone_number
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    ### Send Staus Order
    def isSendStatusOrder(self):
        while True:
            is_send_status = input(colored('Do you want to send status order? [Y/N]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if is_send_status.upper() == 'Y':
                return True
            elif is_send_status.upper() == 'N':
                return False
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def chooseMethodExportStatus(self):
        while True:
            method_export = input(colored('Please choose method send (Telegram/Zalo/Messenger) [T/Z/M]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if method_export.upper() not in ['T','Z','M']:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')
            else:
                chatapp_instance, chatapp_strategy = None, None
                if method_export.upper() in ['T','Z']:
                    phone_number = self.getPhoneNumber()
                    if method_export.upper() == 'T':
                        chatapp_instance = TelegramFactory.getInstance()
                    else:
                        chatapp_instance = ZaloFactory.getInstance()
                    chatapp_strategy = chatapp_instance.createStrategy(phone_number) 
                elif method_export.upper() == 'M':
                    id = input(colored('Please enter your id: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
                    chatapp_instance = MessengerFactory.getInstance()
                    chatapp_strategy = chatapp_instance.createStrategy(id) 
                
                status_visitor.cas = chatapp_strategy # Set strategy
                return
                
        

    ## Print bill
    def isPrintBill(self):
        while True:
            is_print_bill = input(colored('Do you want to print bill? [Y/N]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if is_print_bill.upper() == 'Y':
                return True
            elif is_print_bill.upper() == 'N':
                return False
            else:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')

    def chooseMethodPrint(self):
        while True:
            method_print = input(colored('Please choose method print (Printer/Telegram/Zalo/Messenger) [P/T/Z/M]: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
            if method_print.upper() not in ['P','T','Z','M']:
                if self.file_mode:
                    raise InvalidInput('Your input is not valid!')
                cprint("Your input is not valid! Please try again", 'red')
            else:
                export_instance, export_strategy = None, None
                if method_print.upper() == 'P':
                    export_instance = PrinterFactory.getInstance()
                    export_strategy = export_instance.createStrategy() 
                elif method_print.upper() in ['T','Z']:
                    phone_number = self.getPhoneNumber()
                    if method_print.upper() == 'T':
                        export_instance = TelegramFactory.getInstance()
                    else:
                        export_instance = ZaloFactory.getInstance()
                    export_strategy = export_instance.createStrategy(phone_number) 
                elif method_print.upper() == 'M':
                    id = input(colored('Please enter your id: ', 'blue', attrs=['blink'])) if self.file_mode == False else self.getNextLine()
                    export_instance = MessengerFactory.getInstance()
                    export_strategy = export_instance.createStrategy(id) 

                BillExport.print_bill(export_strategy)
                return

    def run(self):
        if self.file_mode:
            with suppress_stdout(): # Silence mode
                return self.main()
        
        return self.main()

    def main(self):
        while True:
            PrintCoffee(self.data['coffee']).accept(PrintMenu())

            coffee_id = self.getCoffeeInput()
            new_coffee = self.getCoffeeById(coffee_id)

            coffee_quantity = self.getCoffeeQuantity(1,new_coffee['quantity'])

            new_coffee['quantity'] = coffee_quantity
            for coffee in self.data['coffee']:
                if coffee['id'] == coffee_id:
                    coffee['quantity'] -= coffee_quantity

            new_coffee['topping'] = []
            while True:
                is_topping_continue = self.isToppingContinue()
                if is_topping_continue == False:
                    break

                PrintTopping(self.data['topping']).accept(PrintMenu())

                topping_id = self.getToppingInput()
                new_topping, is_new = self.getToppingById(new_coffee, topping_id)

                topping_quantity = self.getToppingQuantity(1, new_topping['quantity'], coffee_quantity)

                new_topping['quantity'] = topping_quantity
                for topping in self.data['topping']:
                    if topping['id'] == topping_id:
                        topping['quantity'] -= topping_quantity * coffee_quantity
                
                if is_new: 
                    new_coffee['topping'].append(new_topping)

            self.cart.append(new_coffee)
            
            is_coffee_continue = self.isCoffeeContinue()
            if is_coffee_continue == False:
                break
        
        total_price = self.calcCartTotal(self.cart)
        # Done

        PrintCart(self.cart, total_price).accept(PrintMenu())

        status_visitor.sendStatus() # Timer starts here
        is_send_status = self.isSendStatusOrder()
        if is_send_status:
            status_visitor.is_disable = False
            self.chooseMethodExportStatus()
            if self.file_mode:
                status_visitor.cancelStatus()
        else:
            status_visitor.cancelStatus()
        
        is_print_bill = self.isPrintBill()
        if is_print_bill:
            self.chooseMethodPrint()
        
        return self.data, self.cart, total_price
        


if __name__ == "__main__":
    ### Run manually
    CoffeeSystem().run()

    ### Run from file
    # (data, cart, total_price) = CoffeeSystem('Testcases/_demofile.txt').run()
    # print(data, '\n')
    # print(cart, '\n')
    # print(total_price)