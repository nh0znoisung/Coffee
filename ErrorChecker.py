class InvalidInput(Exception):
    def __init__(self,msg):
	    # msg:string
        self.s = msg

    def __str__(self):
        return "Invalid Input: " + self.s +"\n"

class OutOfRange(Exception):
    def __init__(self,msg):
	    # msg:string
        self.s = msg

    def __str__(self):
        return "Out of range: " + self.s +"\n"

class NoItem(Exception): pass