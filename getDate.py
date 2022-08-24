import requests
import json

r = requests.get('https://api.covid19api.com/summary')
rText = r.text
rData = r.json()
Global = rData["Global"]
data = rData["Countries"]
#print(Global)
#print(type(len(data)))

def func(x):
    for i in range(len(data)):
        if x == data[i]["Slug"]:
            text = f'Country: {str(data[i]["Country"])}'
            print(text)


if __name__ == "__main__":
    x = str(input("Enter command: "))
    func(x)