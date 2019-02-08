'''
Created on 19.01.2014

@author: Klaus Ummenhofer
'''

# Import Functionality of Analog Output Module
from lucidIo.LucidControlAO4 import LucidControlAO4

# Import Value Type for reading an writing of currents
from lucidIo.Values import ValueCUS4

# Import LucidControl return values
from lucidIo import IoReturn 


if __name__ == '__main__':

    print( 'START EXAMPLE')
    
    # Create AO4 object using COM8
    # For Linux OS \dev\ttyACM0 (with 0 as the number of the interface)
    ao4 = LucidControlAO4('COM3')
    
    # Open AO4 port
    if (ao4.open() == False):
        print( 'Error connecting to port {0} '.format( ao4.portName ))
        ao4.close()
        exit()
    
    print( 'PORT OPENED')
    
    print( '=========================================================================')
    print( ' IDENTIFY DEVICE')
    print( '=========================================================================')
    
    ret = ao4.identify(0)
    
    if ret == IoReturn.IoReturn.IO_RETURN_OK:
        print( 'Device Class:       {0}'.format(ao4.getDeviceClassName()))
        print( 'Device Type:        {0}'.format(ao4.getDeviceTypeName()))
        print( 'Serial No.:         {0}'.format(ao4.getDeviceSnr()))
        print( 'Firmware Rev.:      {0}'.format(ao4.getRevisionFw()))
        print( 'Hardware Rev.:      {0}'.format(ao4.getRevisionHw()))
    else:
        print( 'Identify Error')
        ao4.close()
        exit()

    print( '=========================================================================')
    print( ' SET CHANNEL 0 to 12.5 mA')
    print( '=========================================================================')
    
    # Create a value object for value type CUS4
    # 4 bytes signed value
    value = ValueCUS4()
    
    # Set current to 12.5mA
    value.setCurrent(12.50)
    
    # Write value to channel 0
    ret = ao4.setIo(0, value)

    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'Set CH0 to {0} mA'.format(value.getCurrent()))
    else:
        print( 'Error setting CH0 current')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' READ BACK CURRENT VALUE OF CHANNEL 0')
    print( '=========================================================================')
    
    # Initialize new value object for the value type CUS4
    value = ValueCUS4()
    value.setCurrent(0)
    
    # Read value of channel 0
    ret = ao4.getIo(0, value)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'CH0 current is {0} mA'.format(value.getCurrent()))
    else:
        print( 'Error reading CH0 current')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' SET CH1 = 7.5mA, CH2 = 10mA, CH3 = 15V AS GROUP')
    print( '=========================================================================')
    
    # Create a tuple of 4 current objects
    values = (ValueCUS4(), ValueCUS4(), ValueCUS4(), ValueCUS4())
    
    # Initialize a boolean tuple for channels to change. CH0 is not changed
    # and remains at previous current of 12.50mA
    channels = (False, True, True, True) 
    
    # Initialize the value objects
    values[0].setCurrent(0)     # CH0 is not changed, value is skipped
    values[1].setCurrent(7.5)
    values[2].setCurrent(10)
    values[3].setCurrent(15)
    
    # Write the values to the module
    ret = ao4.setIoGroup(channels, values)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'Set CH1 to {0} mA, CH2 to {1} mA and CH3 to {2} mA'.format( values[1].getCurrent(), values[2].getCurrent(), values[3].getCurrent()))
    else:
        print( 'Error setting CH1, CH2 and CH3 current')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' READ BACK CURRENT VALUES OF CH0, CH1, CH2 AND CH3 AS GROUP')
    print( '=========================================================================')
    
    # Create a tuple of 4 current objects
    values = (ValueCUS4(), ValueCUS4(), ValueCUS4(), ValueCUS4())
    
    # Initialize a boolean tuple for channels to read.
    channels = (True, True, True, True)
    
    # Read the values of all current channels
    ret = ao4.getIoGroup(channels, values)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'CH0 is {0} mA, CH1 is {1} mA, CH2 is {2} mA, CH3 is {3} mA'.format(
            values[0].getCurrent(), values[1].getCurrent(),
            values[2].getCurrent(), values[3].getCurrent()))
    else:
        print( 'Error reading CH0, CH1, CH2 and CH3 currents')
        ao4.close()
        exit()
    
    print( 'END EXAMPLE'  )

