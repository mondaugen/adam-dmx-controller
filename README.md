Requires DmxPy in PYTHONPATH, e.g., do

PYTHONPATH="./DmxPy:${PYTHONPATH}" ...

before running in this directory so Python knows where the module is.

For a simple test, run (on OSX, Unix)

    PYTHONPATH="./DmxPy:${PYTHONPATH}" python light_routine_test.py

The above commands must be run from the directory containing this README file.

# How to run on Windows (deprecated)

Open command-prompt as ***administrator*** (right-click on Command Prompt and select run as administrator)

navigate to adam-dmx-controller

To run the installation, run:

run_light_routine.bat

To run a test, run:

run_light_routine_fastmode.bat

# To adjust the parameters look in light_control.py

# How to run with Lucid IO on Windows

## Install dependencies
- you need to have Python 2 installed
- pyLucidIo-2.1 (downloadable from https://www.lucid-control.com/wp-content/uploads/Software/LucidControlAPI/PyLucidIo/2.1/pyLucidIo-2.1.zip)
	- unzip pyLucidIo-2.1 to the folder above the one this README is in
- then run install_dependencies.bat

## Run batch file
simply run run_light_routine_lucid.bat
### Configuration
Values in run_light_routine_lucid.bat can be adjusted.

## Calibration
You can choose the transfer function exponent by running

py -2 lucid_calibration_ramp.py 10

Here 10 would be the exponent, you can try different values.

To then change this value to be the permanent exponent, change the appropriate value in run_light_routine_lucid.bat

