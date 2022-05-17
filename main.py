import json

def read_json(filename):
    with open(filename) as f:
        data = json.load(f)
        return data

def main():
    x = input("Enter a number: ")
    while(x != "a"):
        print(x)
        x = input("Enter a number: ")

if __name__ == "__main__":
    print(read_json('data.json'))
    main()