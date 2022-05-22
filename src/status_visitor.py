from threading import Timer
from termcolor import cprint, colored
from dataclasses import dataclass
from export_strategy import *

STATUS_PENDING_MESSAGE = "Your order is in queue"
STATUS_PROCESSING_MESSAGE = "Your order is in process"
STATUS_COMPLETE_MESSAGE = "Your order is done"

DELAY_PENDING = 15
DELAY_PROCESSING = 20
DELAY_COMPLETE = 30

is_disable = True # Disable Timer
cas = None #ChatappStrategy

@dataclass # Make sure order of field same in contructor 
class Status:
    def accept(self, v):
        return v.visit(self)

@dataclass
class StatusPending(Status):
    message: str = STATUS_PENDING_MESSAGE
    delay: int = DELAY_PENDING

@dataclass
class StatusProcessing(Status):
    message: str = STATUS_PROCESSING_MESSAGE
    delay: int = DELAY_PROCESSING
    
@dataclass
class StatusComplete(Status):
    message: str = STATUS_COMPLETE_MESSAGE
    delay: int = DELAY_COMPLETE


@dataclass
class Visitor:
    def visit(self, status: Status): pass

@dataclass
class PrintStatus(Visitor):
    def visit(self, status: Status):
        color = None
        if type(status) is StatusPending:
            color = 'red'
        elif type(status) is StatusProcessing:
            color = 'yellow'
        elif type(status) is StatusComplete:
            color = 'green'
        def printStatus():
            if is_disable == False and cas is not None:
                print()
                cas.print_status_order()
                cprint(status.message, color, 'on_grey', attrs=['bold', 'blink'])
                
        return printStatus

@dataclass
class CreateTimer(Visitor):
    def visit(self, status: Status):
        timer = Timer(status.delay, status.accept(PrintStatus()))
        return timer

@dataclass
class StartTimer(Visitor):
    def visit(self, status: Status):
        timer = status.accept(CreateTimer())
        timer.start()
        return timer
    

timer_pending, timer_processing, timer_complete = None, None, None

# after the delay seconds, Message will be printed
def sendStatus():
    global timer_pending, timer_processing, timer_complete
    start_timer = StartTimer()

    status_pending = StatusPending()
    status_processing = StatusProcessing()
    status_complete = StatusComplete()

    timer_pending =  status_pending.accept(start_timer)
    timer_processing = status_processing.accept(start_timer)
    timer_complete =  status_complete.accept(start_timer)

def cancelStatus():
    global timer_pending, timer_processing, timer_complete
    
    timer_pending.cancel()
    timer_processing.cancel()
    timer_complete.cancel()
