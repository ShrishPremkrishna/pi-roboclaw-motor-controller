from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servoBarLift = Servo(1, pin_factory=factory)
servoGripper = Servo(4, pin_factory=factory)

servoBarLift.detach()
servoGripper.detach()






