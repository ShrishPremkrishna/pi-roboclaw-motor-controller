from roboclaw import Roboclaw
from time import sleep

# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

# cd ~/robotics/pi-roboclaw-motor-controller/roboclaw_packet_serial
# python3 packet_serial.py

if __name__ == "__main__":
    
    address = 0x80
    roboclaw = Roboclaw("/dev/serial0", 115200)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')
    
    while True:
        
        print('64 - M1 Forward')
        roboclaw.ForwardM1(address,64)
        sleep(2)
        print('0 - M1 Forward')
        roboclaw.ForwardM1(address,0)
        sleep(2)
        
        print('64 - M2 Forward')
        roboclaw.ForwardM2(address, 64)
        sleep(2)
        print('0 - M2 Forward')
        roboclaw.ForwardM2(address,0)
        sleep(2)

        break

    
    

