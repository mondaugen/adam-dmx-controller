import light_control as lc
import os

if 'USE_DMX' in os.environ:
    lctr=lc.light_conductor_c(lc.light_ctl_low_level_dmx("COM4"),fastmode=1)
elif 'USE_LUCIDIO' in os.environ:
    lctr=lc.light_conductor_c(
        lc.light_ctl_low_level_lucid(
        transfer_function=lc.x_p_transfer_function(3),
        interface_path="/dev/ttyACM0",
        verbose=True),
        fastmode=0)

lctr.test_routine()
