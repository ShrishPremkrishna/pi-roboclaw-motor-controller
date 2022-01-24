from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

from pyPS4Controller.controller import Controller

factory = PiGPIOFactory()

servoBarLift = Servo(17, pin_factory=factory)
servoGripper = Servo(22, pin_factory=factory)


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    #
    def on_triangle_press(self):
        print('Bar Lift Up')
        servoBarLift.value = 0.8

    #
    def on_x_press(self):
        print('Bar Lift Down')
        servoBarLift.min()
        servoBarLift.detach()

    #
    def on_square_press(self):
        print('Gripper Open')
        servoGripper.value = 0.5

    #
    def on_circle_press(self):
        print('Gripper Close')
        servoGripper.value = -0.5
        servoGripper.detach()


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=6)  



