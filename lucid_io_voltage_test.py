'''
Created on 19.01.2014

@author: Klaus Ummenhofer
'''

# Import Functionality of Analog Output Module
from lucidIo.LucidControlAO4 import LucidControlAO4

# Import Value Type for reading an writing of voltages
from lucidIo.Values import ValueVOS4

# Import LucidControl return values
from lucidIo import IoReturn 


if __name__ == '__main__':

    print( 'START EXAMPLE')
    
    # Create AO4 object using COM8
    # For Linux OS \dev\ttyACM0 (with 0 as the number of the interface)
    ao4 = LucidControlAO4('COM3')
    
    # Open AO4 port
    if (ao4.open() == False):
        print( 'Error connecting to port {0} '.format(ao4.portName))
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
    print( ' SET CHANNEL 0 to 2.50 V')
    print( '=========================================================================')
    
    # Create a value object for value type VOS4
    # 4 bytes signed value
    value = ValueVOS4()
    
    # Set voltage to 1.25 V
    value.setVoltage(0.2)
    
    # Write value to channel 0
    ret = ao4.setIo(0, value)

    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'Set CH0 to {0} V'.format(value.getVoltage()))
    else:
        print( 'Error setting CH0 voltage')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' READ BACK VOLTAGE VALUE OF CHANNEL 0')
    print( '=========================================================================')
    
    # Initialize new value object for the value type VOS4
    value = ValueVOS4()
    value.setVoltage(0)
    
    # Read value of channel 0
    ret = ao4.getIo(0, value)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'CH0 voltage is {0} V'.format(value.getVoltage()))
    else:
        print( 'Error reading CH0 voltage')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' SET CH1 = 1.25V, CH2 = 2.50V, CH3 = 5.00V AS GROUP')
    print( '=========================================================================')
    
    # Create a tuple of 4 voltage objects
    values = (ValueVOS4(), ValueVOS4(), ValueVOS4(), ValueVOS4())
    
    # Initialize a boolean tuple for channels to change. CH0 is not changed
    # and remains at previous voltage of 2.50V
    channels = (False, True, True, True) 
    
    # Initialize the value objects
    values[3].setVoltage(0)     # CH0 is not changed, value is skipped
    values[2].setVoltage(0)
    values[1].setVoltage(0)
    values[0].setVoltage(0)
    
    # Write the values to the module
    ret = ao4.setIoGroup(channels, values)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'Set CH1 to {0} V, CH2 to {1} V and CH3 to {2} V'.format( values[1].getVoltage(), values[2].getVoltage(), values[3].getVoltage()))
    else:
        print( 'Error setting CH1, CH2 and CH3 voltage')
        ao4.close()
        exit()
    
    print( '=========================================================================')
    print( ' READ BACK VOLTAGE VALUE OF CH0, CH1, CH2 AND CH3 AS GROUP')
    print( '=========================================================================')
    
    # Create a tuple of 4 voltage objects
    values = (ValueVOS4(), ValueVOS4(), ValueVOS4(), ValueVOS4())
    
    # Initialize a boolean tuple for channels to read.
    channels = (True, True, True, True)
    
    # Read the values of all voltage channels
    ret = ao4.getIoGroup(channels, values)
    
    # Check return value for success
    if (ret == IoReturn.IoReturn.IO_RETURN_OK):
        print( 'CH0 is {0} V, CH1 is {1} V, CH2 is {2} V, CH3 is {3} V'.format( values[0].getVoltage(), values[1].getVoltage(), values[2].getVoltage(), values[3].getVoltage()))
    else:
        print( 'Error reading CH0, CH1, CH2 and CH3 voltages')
        ao4.close()
        exit()
    
    print( 'END EXAMPLE'  )
