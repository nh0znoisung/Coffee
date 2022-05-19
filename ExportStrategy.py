from dataclasses import dataclass
from termcolor import cprint

#   Context: strategy -> setStrategy(),context.doSth()

####  Strategy
@dataclass
class ExportStrategy: 
    def print_bill(self): pass

@dataclass
class PrinterStrategy(ExportStrategy):
    def print_bill(self):
        cprint("Printer :", 'red', 'on_cyan', end=" ", attrs=['bold', 'blink'])
        cprint("Your bill have been printed", 'magenta', 'on_grey', attrs=['bold', 'blink'])



@dataclass
class ChatappStrategy(ExportStrategy): 
    def print_status_order(self): pass

@dataclass
class TelegramStrategy(ChatappStrategy):
    phone_number: str

    def print_bill(self):
        cprint("Telegram PhoneNumber-{}:".format(self.phone_number), 'red', 'on_blue', end=" ", attrs=['bold', 'blink'])
        cprint("Your bill have been printed", 'magenta', 'on_grey', attrs=['bold', 'blink'])

    def print_status_order(self):
        cprint("Telegram PhoneNumber-{}:".format(self.phone_number), 'green', 'on_white', end=" ", attrs=['bold', 'blink'])

@dataclass
class ZaloStrategy(ChatappStrategy):
    phone_number: str

    def print_bill(self):
        cprint("Zalo PhoneNumber-{}:".format(self.phone_number), 'blue', 'on_white', end=" ", attrs=['bold', 'blink'])
        cprint("Your bill have been printed", 'magenta', 'on_grey', attrs=['bold', 'blink'])

    def print_status_order(self):
        cprint("Zalo PhoneNumber-{}:".format(self.phone_number), 'green', 'on_white', end=" ", attrs=['bold', 'blink'])

@dataclass
class MessengerStrategy(ChatappStrategy):
    id: str

    def print_bill(self):
        cprint("Messenger ID-{}:".format(self.id), 'green', 'on_white', end=" ", attrs=['bold', 'blink'])
        cprint("Your bill have been printed", 'magenta', 'on_grey', attrs=['bold', 'blink'])

    def print_status_order(self):
        cprint("Messenger ID {}:".format(self.id), 'green', 'on_white', end=" ", attrs=['bold', 'blink'])

