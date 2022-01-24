from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servo = Servo(17, pin_factory=factory)

while True:
    servo.value = -1
    sleep(1)
    # servo.value = 0
    sleep(1)
    servo.value = 20
    sleep(4)

    servo.detach()
    break

