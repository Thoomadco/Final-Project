import requests
from win10toast import ToastModifier
import json
import time
def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'case:{data["cases"]} \nDeaths:{data["deaths"]} \nRecovered:{data["recovered"]}'

    while True:
        t=ToastModifier()
        t.show_toast("Covid_19 Update",text,duration=15)
        time.sleep(30)
update()
