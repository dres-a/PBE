import threading
import time


class clase:
    def __init__(self):
        self.arg = "Buenas"
                 

    def CambioArg(self):
        self.arg = "tardes"


c = clase()

print(c.arg)
thread = threading.Thread(target = c.CambioArg)
thread.start()
time.sleep(2)
print(c.arg)
