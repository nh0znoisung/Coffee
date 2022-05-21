import json
from ErrorChecker import *

FILE_DATA = './data.json'

def getData(filename: str)-> dict:
    # Open file and read data
    with open(filename) as f:
        data = json.load(f)
        f.close()
    return data

def dataPreprocessing(data: dict) -> list:
    # Coverting dict data to list of tuples
    return list(map(lambda x: (x['id'], x['name'], x['quantity'], x['price']), data))

def checkRangeInteger(txt: str, low: int, high: int)->bool:
    num = int(txt)
    if num < low or num > high:
        raise OutOfRange('Your input is out of range!')
    return True
