import time

# Import Functionality of Analog Output Module
from lucidIo.LucidControlAO4 import LucidControlAO4

# Import Value Type for reading an writing of voltages
from lucidIo.Values import ValueVOS4

# Import LucidControl return values
from lucidIo import IoReturn


def setup():
    # Create AO4 object using COM3
    # For Linux OS \dev\ttyACM0 (with 0 as the number of the interface)
    ao4 = LucidControlAO4('COM3')
    
    # Open AO4 port
    if (ao4.open() == False):
        print( 'Error connecting to port {0} '.format(ao4.portName))
        ao4.close()
        exit()
    return ao4

def set_voltage(val,device,channel=0):
    value = ValueVOS4()
    
    # Set voltage to 1.25 V
    value.setVoltage(val)
    
    # Write value to channel 0
    ret = device.setIo(channel, value)

lighting_controller=setup()

ramp_val = 0
ramp_step = 0.01
ramp_wait=0.1
ramp_max=1

try:
    while  True:
        set_voltage(ramp_val,lighting_controller)
        print("voltage: %f" % (ramp_val,))
        ramp_val += ramp_step
        if ramp_val > ramp_max:
            ramp_val = 0
        time.sleep(ramp_wait)
except KeyboardInterrupt:
    pass

lighting_controller.close()
