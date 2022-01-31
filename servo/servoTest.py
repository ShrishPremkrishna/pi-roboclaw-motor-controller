from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servoBarLift = Servo(22, pin_factory=factory)
servoGripper = Servo(17, pin_factory=factory)

servoBarLift.value = 0.75
sleep(3)
servoBarLift.value = -0.75
sleep(3)

servoBarLift.detach()
servoGripper.detach()






