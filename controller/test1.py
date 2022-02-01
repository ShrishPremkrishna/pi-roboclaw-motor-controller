from time import sleep
from roboclaw import Roboclaw

address128 = 0x80
address129 = 0x81
address130 = 0x82

roboclaw = Roboclaw("/dev/serial0", 38400)
result = roboclaw.Open()
if result == 0:
    print('Unable to open port')

while True:
    roboclaw.ForwardM1(address129, 20)
    roboclaw.ForwardM2(address129, 20)
    roboclaw.ForwardM1(address128, 20)
    roboclaw.ForwardM2(address128, 20)
    sleep(5)
    break