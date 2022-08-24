from datetime import datetime
import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://api.covid19api.com/summary').json()
    data = r["Global"]
    date = datetime.datetime.now().date()
    text = f'Date: {date} \nNew Confirmed: {data["NewConfirmed"]} \nTotal Confirmed: {data["TotalConfirmed"]} \nNew Deaths: {data["NewDeaths"]} \nTotal Deaths: {data["TotalDeaths"]} \nNew Recovered: {data["NewRecovered"]} \nTotal Recovered: {data["TotalRecovered"]}'

    while True:
        t = ToastNotifier()
        t.show_toast("Covid 19 Update", text, duration=20)
        time.sleep(1)

if __name__ == "__main__":
    update()