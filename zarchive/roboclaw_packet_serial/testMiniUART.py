import serial


# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

serialport = serial.Serial("/dev/serial0", baudrate=9600, timeout=3.0)
print(serialport.name)
while True:
    serialport.write(b'hello')
    rcv = serialport.read(10)
    print(rcv)
    serialport.write(('rnYou sent:' + repr(rcv)).encode('utf-8'))