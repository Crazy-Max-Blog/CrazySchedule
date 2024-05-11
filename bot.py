from requests import get
import time, os

d={}
m={}

getData()

os.environ['TZ'] = d['TZ']
dt=time.strftime("%d.%m.%Y")
time.tzset()
print(time.strftime("%H.%M"))

def sendMsg(text):
    get(f'https://api.telegram.org/bot{d["TOKEN"]}/sendMessage?chat_id={d["ID"]}&text={text}')


def getData():
    global dt
    with open('data/base.json', 'r', encoding='utf-8') as b:
        exec(f'global d;d={b.read()}')

    with open(f'data/date/{dt}.json', 'r', encoding='utf-8') as b:
        exec(f'global m;m={b.read()}')

while True:
    getData()
    dt=time.strftime("%d.%m.%Y")
    t=time.strftime("%H:%M")
    if t in m:
        s=m[t]
        print(s)
        sendMsg(s)
        time.sleep(60)
    else:
        time.sleep(1)
