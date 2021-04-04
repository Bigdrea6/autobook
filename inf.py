import time
import datetime

import login

def hei():
    while True:
        dt_now = datetime.datetime.now()
        s_1=10
        s_2=19
        h=dt_now.hour
        m=dt_now.minute
        if s_1==h or s_2==h:
            kekka=go()
            if kekka=='Fin':
                break
            else:
                return kekka
        else:
            time.sleep(120)

def kyuu():
    while True:
        dt_now = datetime.datetime.now()
        s_1=10
        s_2=18
        h=dt_now.hour
        m=dt_now.minute
        if s_1==h or s_2==h:
            kekka=go()
            if kekka=='Fin':
                break
            else:
                return kekka

        else:
            time.sleep(120)

def go():
    for i in range(40):
        log=login.main()
        if log!=None:
            return log
        else:
            False
        time.sleep(170)
    return Fin
