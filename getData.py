import json

def getData(filename: str)-> dict:
    # Open file and read data
    with open(filename) as f:
        data = json.load(f)
        f.close()
    return data

def dataPreprocessing(data: dict) -> list:
    # Coverting dict data to list of tuples
    return list(map(lambda x: (x.get('id'), x['name'], x['quantity'], x['cost']), data))