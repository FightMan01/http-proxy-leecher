import requests
import threading
import signal
import time
import os

szal = int(input("Szálak: "))

def getListProxy():
    url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    res = requests.get(url)
    return res.text, res.status_code

class fő(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tasks = []
        self.res = res
        self.stcod = stcod
        self.pr = pr
    def run(self):
        typ = "http"
        anon = ""
        country = ""
        if(self.stcod == 200 and self.res):
            for i in range(len(self.pr)):
                try:
                    cur = self.pr.pop(i)
                except:
                    exit(0)
                x = cur.replace("\r", "")
                print(f'\033[0m[{x}] ~> Proxy ellenőrzése...')
                try:
                    r = requests.get("http://ipinfo.io/json", proxies={'http':'http://' + x}, timeout=5)
                    print(f'\033[0m[{x}] ~> Proxy érvényes!')
                    f = open('proxies.txt', 'a')
                    f.write(f"\n{x}")
                    f.close()
                except requests.exceptions.ConnectionError as e:
                    print(f'\033[91m[{x}] ~> Hiba!')
                    continue
                except requests.exceptions.ConnectTimeout as e:
                    print(f'\033[91m[{x}] ~> Időtúllépési hiba!')
                    continue
                except requests.exceptions.HTTPError as e:
                    print(f'\033[91m[{x}] ~> HTTP hiba!')
                    continue
                except requests.exceptions.Timeout as e:
                    print(f'\033[91m[{x}] ~> Időtúllépési hiba!')
                    continue
                except requests.exceptions.TooManyRedirects as e:
                    print(f'\033[91m[{x}] ~> Túl sok átirányítás!')
                    continue
                except:
                    print(f'\033[91m[{x}] ~> Ismeretlen hiba!')
                    continue

if __name__ == '__main__':
    global res, stcod
    res, stcod = getListProxy()
    global pr 
    pr = res.split('\n')
    threads = []
    for x in range(szal):
        threads.append(fő())
    for thread in threads:
        thread.daemon = True
        thread.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\033[0m\nKilépés...")
        exit(0)