import time

# Import Functionality of Analog Output Module
from lucidIo.LucidControlAO4 import LucidControlAO4

# Import Value Type for reading an writing of voltages
from lucidIo.Values import ValueVOS4

# Import LucidControl return values
from lucidIo import IoReturn

import threading

# MUST be power of 2
N_PWM_STEPS=256
PWM_PERIOD=1e-6

class LucidPWMCtl(threading.Thread):
    def run(self):
        self._running = True
        while self._running:
            value = ValueVOS4()
            if self.cur_step < self._duty:
                value.setVoltage(self.brightness)
            else:
                value.setVoltage(0)
            self.light_controller.setIo(self.channel, value)
            self.cur_step = (self.cur_step + 1) & (N_PWM_STEPS - 1)
            #print(self.cur_step)
            time.sleep(PWM_PERIOD)
    def __init__(self,port='COM3',brightness=10,channel=0):
        threading.Thread.__init__(self)
        self.light_controller = LucidControlAO4('COM3')
        # Open AO4 port
        if (self.light_controller.open() == False):
            raise IOError( 'Error connecting to port {0} '.format(self.light_controller.portName) )
        self.cur_step = 0
        self.brightness = brightness
        self.channel = channel
        # Initially light is off
        self._duty = 0
    def set_fade(self,val):
        """ Sets fade value between 0 and 1 inclusive (0 is off, 1 is on all the time) """
        self._duty = int(N_PWM_STEPS * val)
    def stop(self):
        self._running = False
        self.join()

lpwmctl = LucidPWMCtl()
lpwmctl.start()

fade = 0
fade_inc = 0.01
wait = 0.5

#try:
#    while fade < 1:
#        lpwmctl.set_fade(fade)
#        print(lpwmctl._duty)
#        fade += fade_inc
#        time.sleep(wait)
#except KeyboardInterrupt:
#    pass    

lpwmctl.set_fade(0.5)

try:
    while True:
        time.sleep(wait)
except KeyboardInterrupt:
    pass

lpwmctl.stop()

