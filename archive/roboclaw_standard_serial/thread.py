import threading
from serial import Serial
from time import sleep
import RPi.GPIO as GPIO

def run_controller(pin, speed, run_time):
    
    GPIO.output(pin, GPIO.HIGH)
    sleep(.2)
    roboclaw.write(bytes([speed]))
    sleep(run_time)
    roboclaw.write(bytes([0]))
    sleep(.2)
    GPIO.output(pin, GPIO.LOW)
    

if __name__ == "__main__":
    
    GPIO.cleanup()
    
    #Configure serial
    
    serial_port = "/dev/ttyS0"
    baudrate = 38400
    roboclaw = Serial(serial_port, baudrate, timeout=1)
    
    #Configure GPIO
    
    slave_select_pins = [25]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(slave_select_pins, GPIO.OUT, initial=GPIO.LOW)
    

    def topleftforward():
        print("topleft forward 94 speed")
        run_controller(25, 94, 2)

    def toprightforward():
        print("topright forward 94 speed")
        run_controller(25, 200, 2)


    # threading.Thread(target=a).start()
    # threading.Thread(target=b).start()

    # # while(1):
        
    # #     run_controller(23, 94, 0)
    # #     run_controller(23, 180, 0)
    # #     sleep(2)

    
#Imports
from time import sleep
from pyPS4Controller.controller import Controller
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

#Event Based Coding
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


    # Chassis controls
        #Move down
    def on_R3_down(self, arg):
        print('Move backward: ' + str(round(arg)))
        # topleftforward()
        # toprightforward()



        #Move forward
    def on_R3_up(self, arg):
        print('Move forward: ' + str(round(arg)))
        

        # TODO

        
        #Move Left
    def on_R3_left(self, arg):
        print('Move left: ' + str(round(arg)))
        # TODO

        
        #Move Right
    def on_R3_right(self, arg):
        print('Move right: ' + str(round(arg)))
        # TODO


    #motor kill
        #Motor stop at y rest on R3
    def on_R3_y_at_rest(self):
        print("r3 rest")
     
        #Motor stop at x rest on R3
    def on_R3_x_at_rest(self):
        print("r3 rest")
   
    def on_share_press(self):
        print("share press")


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=10)    
