from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servoBarLift = Servo(17, pin_factory=factory)
servoGripper = Servo(22, pin_factory=factory)

servoBarLift.detach()
servoGripper.detach()


