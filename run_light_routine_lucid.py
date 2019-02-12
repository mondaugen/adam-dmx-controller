# runs the routine forever using LucidIO
import os
os.environ['USE_LUCIDIO']='1'
import light_control as lc
import sys
import time
import serial
import time

SLEEP_BETWEEN_ERR_AND_CYCLE_S = 5

if 'VERBOSE' in os.environ:
    verbose=True
else:
    verbose=False

fastmode=0
if len(sys.argv) >= 2:
  fastmode=int(sys.argv[1])

if fastmode and verbose:
  print "running in fastmode"

DEFAULT_ADDR='COM3'

if 'LUCID_ADDR' not in os.environ:
    print("Using default address %s\n" % (DEFAULT_ADDR,))
    lucid_addr=DEFAULT_ADDR
else:
    lucid_addr=os.environ['LUCID_ADDR']
if verbose:
    print("Lucid address %s" % (lucid_addr,))

if 'TRANSFER_FUNCTION_EXPONENT' not in os.environ:
    transfer_function_exponent=1.
else:
    transfer_function_exponent=float(os.environ['TRANSFER_FUNCTION_EXPONENT'])
if verbose:
    print("Transfer function exponent %f" % (transfer_function_exponent,))

while True:
    try:
        lctr=lc.light_conductor_c(
            lc.light_ctl_low_level_lucid(
            transfer_function=lc.x_p_transfer_function(transfer_function_exponent),
            interface_path=lucid_addr,
            verbose=verbose),
            fastmode=fastmode)
        while True:
            lctr.full_routine_iteration(verbose=verbose)
    except Exception as e:
        print 'ERR!',e
        time.sleep(SLEEP_BETWEEN_ERR_AND_CYCLE_S)
