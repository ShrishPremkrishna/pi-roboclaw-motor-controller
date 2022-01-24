from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

from roboclaw import Roboclaw
from pyPS4Controller.controller import Controller

factory = PiGPIOFactory()

servoBarLift = Servo(17, pin_factory=factory, max = 0.8)
servoGripper = Servo(22, pin_factory=factory)


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    #
    def on_triangle_press(self):
        print('Bar Lift Up')
        servoBarLift.max()

    #
    def on_x_press(self):
        print('Bar Lift Down')
        servoBarLift.min()

    #
    def on_square_press(self):
        print('Gripper Open')
        servoGripper.value = 0.5

    #
    def on_circle_press(self):
        print('Gripper Close')
        servoGripper.value = -0.5


servoBarLift.min()
print("min")
sleep(2)

servoBarLift.detach()



