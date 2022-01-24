from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servo = Servo(17, pin_factory=factory)

while True:
    # servo.value = -0.75
    # print("0.75")
    # sleep(1)

    servo.value = 0.75
    servo.value = -0.75
    


    # servo.value = 0.5
    # print ("0.75")
    # sleep(1)

    servo.value = None
    break

