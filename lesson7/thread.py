import time
import threading

def test():
    i = 0
    while True:
        print(i)
        i += 1
        time.sleep(1)

def sec ():
    count = 0
    while True:
        if count % 3 == 0:
            print ("Прошло три секунды")
        count += 1
        time.sleep(1)

def thr ():
    count = 0
    while True:
        if count % 5 == 0:
            print ("Прошло пять секунд")
        count += 1
        time.sleep(1)

t1 = threading.Thread(target=test)
t2 = threading.Thread(target=sec)
t3 = threading.Thread(target=thr)

t1.start()
t2.start()
t3.start()