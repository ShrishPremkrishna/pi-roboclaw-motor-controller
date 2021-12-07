from serial import Serial
from time import sleep

# cd robotics/stacker-bot/raspberry_pi_standard_serial
# python3 standard_serial.py

# sudo nano /boot/config.txt
# sudo nano /boot/cmdline.txt

# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

# sudo usermod -a -G dialout pi
# sudo usermod -a -G tty pi

# groups


if __name__ == "__main__":

    serial_port = "/dev/ttyS0"
    baudrate = 38400
    # baudrate = 115200

    roboclaw = Serial(serial_port, baudrate, timeout=1)
    
    while True:
        print('74 - M1 Forward')
        roboclaw.write(str.encode(chr(74)))
        sleep(1)
        print('64 - M1 Stop')
        roboclaw.write(str.encode(chr(64)))
        sleep(1)
        print('54 - M1 Backward')
        roboclaw.write(str.encode(chr(54)))
        sleep(1)
        print('64 - M1 Stop')
        roboclaw.write(str.encode(chr(64)))
        sleep(1)
        
        print('202 - M2 Forward')
        roboclaw.write(str.encode(chr(202)))
        sleep(1)
        print('192 - M2 Stop')
        roboclaw.write(str.encode(chr(192)))
        sleep(1)
        print('182 - M2 Backward')
        roboclaw.write(str.encode(chr(182)))
        sleep(1)
        print('192 - M2 Stop')
        roboclaw.write(str.encode(chr(192)))
        sleep(1)

        break

# Value	    Function
# 0	        Shuts down channels 1 and 2
# 1	        Channel 1 full reverse
# 64	    Channel 1 stop
# 127	    Channel 1 full forward
# 128	    Channel 2 full reverse
# 192	    Channel 2 stop
# 255	    Channel 2 full forward
