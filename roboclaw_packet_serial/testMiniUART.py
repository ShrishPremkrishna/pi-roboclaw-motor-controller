import serial


# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

serialport = serial.Serial("serial0", baudrate=9600, timeout=3.0)
while True:
    serialport.write("gsm")
    rcv = port.read(10)
    serialport.write("sent:" + repr(rcv))