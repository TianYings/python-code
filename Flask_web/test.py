import json

def main():
    f = open("./config.txt","r")
    d = json.loads(f.read())
    print(d["ip"])
if __name__ == '__main__':
    main()