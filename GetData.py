import json

FILE_DATA = 'data.json'

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
    try:
        num = int(txt)
        if num < low or num > high:
            return False
        return True
    except:
        return False