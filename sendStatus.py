from threading import Timer

def sendStatusMessage():
    print("Your order is ready")

def sendStatus():
    t = Timer(10, sendStatusMessage)
    t.start() # after 10 seconds, Message will be printed

