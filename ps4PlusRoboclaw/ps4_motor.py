from roboclaw import Roboclaw
from time import sleep
from pyPS4Controller.controller import Controller

from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servo = Servo(16, pin_factory=factory)

# sudo chmod 666 /dev/ttyS0
# sudo chmod 666 /dev/serial0
# sudo pigpiod

# cd 
# python3 

if __name__ == "__main__":
    
    address128 = 0x80
    address129 = 0x81
    address130 = 0x82
    roboclaw = Roboclaw("/dev/serial0", 38400)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    #going forward with triangle press for M1
    def on_triangle_press(self):
        print('Linear Slide Up')
        roboclaw.ForwardM1(address130,64)

    #STOP going forward with triangle press for M1
    def on_triangle_release(self):
        print('Linear Slide Stop')
        roboclaw.ForwardM1(address130,0)

    #going forward with up arrow press for M2
    def on_x_press(self):
        print('Linear Slide Down')
        roboclaw.BackwardM1(address130,64)

    #STOP going forward with up arrow press for M2
    def on_x_release(self):
        print('Linear Slide Stop')
        roboclaw.BackwardM1(address130,0)

    #Servo to max
    def on_square_press(self):
        print('servo max')
        servo.max()

    #servo to min
    def on_circle_press(self):
        print("servo min")
        servo.min()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=6)    
