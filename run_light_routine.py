# Just runs the routine forever
import light_control as lc
import sys

fastmode=0
if len(sys.argv) >= 2:
    fastmode=int(sys.argv[1])

if fastmode:
    print "running in fastmode"

lctr=lc.light_conductor_c('/dev/ttyUSB0',fastmode=fastmode)

while True:
    lctr.full_routine_iteration()
