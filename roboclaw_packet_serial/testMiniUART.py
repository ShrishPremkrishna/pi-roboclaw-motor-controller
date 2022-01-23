import serial


# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

serialport = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
print ('latest')
while True:
    serialport.write(str.encode('rnSay something:'))
    serialport.write(bytes([10]))
    rcv = serialport.read(10)
    print('rcv' + rcv);
    serialport.write(str.encode('rnYou sent:' + repr(rcv)))