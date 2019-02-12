import os
os.environ['USE_LUCIDIO']='1'
import light_control as lc
import sys

DEFAULT_ADDR='COM3'

if 'LUCID_ADDR' not in os.environ:
    print("Using default address %s\n" % (DEFAULT_ADDR,))
    lucid_addr=DEFAULT_ADDR
else:
    lucid_addr=os.environ['LUCID_ADDR']

if len(sys.argv) != 2:
    print("Specify transfer function exponent.")
    exit()

p=float(sys.argv[1])

lctr=lc.light_conductor_c(
    lc.light_ctl_low_level_lucid(
    transfer_function=lc.x_p_transfer_function(p),
    interface_path="/dev/ttyACM0",
    verbose=True),
    fastmode=0)

lctr.calibration_ramp()
