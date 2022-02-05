from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servoBarLift = Servo(22, pin_factory=factory)
servoGripper = Servo(17, pin_factory=factory)


servoBarLift.value = -1
sleep(3)
servoBarLift.value = 0
sleep(2)
servoBarLift.value = 0.8
sleep(3)
servoBarLift.value = 0
sleep(2)


servoBarLift.detach()
servoGripper.detach()






