Requires DmxPy in PYTHONPATH, e.g., do

PYTHONPATH="./DmxPy:${PYTHONPATH}" ...

before running in this directory so Python knows where the module is.

For a simple test, run (on OSX, Unix)

    PYTHONPATH="./DmxPy:${PYTHONPATH}" python light_routine_test.py

on Windows, run (not tested)

    set PYTHONPATH=%PYTHONPATH%;.\DmxPy
    py -2 light_routine_test.py

The above commands must be run from the directory containing this README file.
