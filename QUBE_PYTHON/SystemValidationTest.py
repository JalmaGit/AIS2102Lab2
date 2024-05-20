from time import time
import math

class SystemValidationTest:
    def __init__(self, volt=12, delay=4):
        self.volt = volt
        self.lastTime = time()
        self.delay = delay
        self.timeSinceLast = time() - self.lastTime

    def stepInput(self):
        if time() < (self.lastTime + self.delay):
            self.volt -= 0.1
            if self.volt <= 0:
                self.volt = 0
            return self.volt
        elif time() < (self.lastTime + self.delay*2):
            self.volt = 24
            return self.volt
        else:
            self.volt = 24
            self.lastTime = time()
            return self.volt
        
    def rampInput(self):
        if time() < (self.lastTime + self.delay):
            
            self.timeSinceLast = time() - self.lastTime
            
            self.volt = 6 * self.timeSinceLast

            if self.volt >= 24:
                self.volt = 24
            return self.volt
        elif time() < (self.lastTime + self.delay*2):
            self.volt = 0
            return self.volt
        else:
            self.volt = 0
            self.lastTime = time()
            return self.volt
        

    def parabolicInput(self):
        if time() < (self.lastTime + self.delay):
            
            self.timeSinceLast = time() - self.lastTime
            
            self.volt = 2 * self.timeSinceLast**2

            if self.volt >= 24:
                self.volt = 24
            return self.volt
        elif time() < (self.lastTime + self.delay*2):
            self.volt = 0
            return self.volt
        else:
            self.volt = 0
            self.lastTime = time()
            return self.volt
    
    def sinuWaveInput(self):
            self.timeSinceLast = time() - self.lastTime
            self.volt = 9 * math.sin(math.pi/4 * self.timeSinceLast) + 9
            return self.volt
        
    def alternatingSpeed(self):
        if time() < (self.lastTime + self.delay):
            speed = 2000 * math.pi/30
            return speed
        elif time() < (self.lastTime + self.delay*2):
            speed = 1000 * math.pi/30
            return speed
        else:
            speed = 1000 * math.pi/30
            self.lastTime = time()
            return speed