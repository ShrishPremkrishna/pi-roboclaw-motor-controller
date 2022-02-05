from roboclaw import Roboclaw
from time import sleep

# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0

# cd roboclaw_packet_serial
# python3 packet_serial.py

if __name__ == "__main__":
    
    address = 0x80
    roboclaw = Roboclaw("/dev/serial0", 38400)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')
    print('Printing connection result - ' + str(result))
    print('Connection - ' + str(roboclaw._port.is_open))
    
    while True:



        version = roboclaw.ReadVersion(address)
        print("Roboclaw Version")
        print(version)

        roboclaw.ResetEncoders(address)
        print(roboclaw.ReadEncM1(address))
        roboclaw.SetEncM1(address, 6000)
        print(roboclaw.ReadEncM1(address))

        # print('\n\n64 - M1 Forward')
        roboclaw.ForwardM1(address,64)
        sleep(0.5)
        # print('\n\n0 - M1 Forward')
        roboclaw.ForwardM1(address, 0)

        # print('64 - M1 Forward')
        # roboclaw.ForwardM1(address,64)

        # sleep(2)

        # print('0 - M1 Forward')
        # roboclaw.ForwardM1(address, 0)


        #M1 forward at 64 speed
        # print('64 - M1 Forward')
        # roboclaw.ForwardM1(address,64)
        #M1 stop going forward
        # print('0 - M1 Forward')
        # roboclaw.ForwardM1(address,0)
        # sleep(2)
        # print('64 - M2 Forward')
        # roboclaw.ForwardM2(address, 64)
        # sleep(2)
        # print('0 - M2 Forward')
        # roboclaw.ForwardM2(address,0)
        # sleep(2)

        # sleep(1)

        # roboclaw.SpeedAccelDeccelPositionM1(address,10000,2000,10000,15000,1)


        
        break

    
    

