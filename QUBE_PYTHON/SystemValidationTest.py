from time import time

class SystemValidationTest:
    def __init__(self, volt=12, delay=4):
        self.volt = volt
        self.lastTime = time()
        self.delay = delay

    def stepInput(self):
        if time() < (self.lastTime + self.delay):
            self.volt -= 0.1
            if self.volt <= 0:
                self.volt = 0
            return self.volt
        elif time() < (self.lastTime + self.delay*2):
            self.volt = 5
            return self.volt
        else:
            self.volt = 5
            self.lastTime = time()
            return self.volt
