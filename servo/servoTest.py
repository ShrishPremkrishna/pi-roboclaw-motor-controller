from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

servo = Servo(17, min_pulse_width=900/1000000, max_pulse_width=2100/1000000, pin_factory=factory, frame_width=20/1000)

while True:
    servo.value = -1
    sleep(1)
    # servo.value = 0
    sleep(1)
    servo.value = 1
    sleep(4)

    servo.detach()
    break

