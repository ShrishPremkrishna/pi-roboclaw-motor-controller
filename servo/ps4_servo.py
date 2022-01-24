from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


factory = PiGPIOFactory()
s = AngularServo(17, min_angle=-42, max_angle=44, pin_factory=factory)

s.angle = max
s.mid()
s.angle = None
