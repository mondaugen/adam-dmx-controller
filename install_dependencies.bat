:: If not already installed, install Python2
py -2 -m pip install pyserial
:: Put pyLucidIo-2.1 in the directory above this one
pushd ..\pyLucidIo-2.1
py -2 setup.py install
popd
