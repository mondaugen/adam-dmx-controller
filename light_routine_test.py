import light_control as lc

lctr=lc.light_conductor_c('/dev/ttyUSB0')

#while True:
#    lctr.full_routine_iteration()

lctr.test_routine()
