from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servoBarLift = Servo(17, pin_factory=factory)
#servoGripper = Servo()

while True:

    servoBarLift.min()
    print("min")
    sleep(2)

    servoBarLift.detach()
    break


