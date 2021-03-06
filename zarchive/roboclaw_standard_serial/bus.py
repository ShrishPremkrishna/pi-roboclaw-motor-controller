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
    
    slave_select_pins = [23]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(slave_select_pins, GPIO.OUT, initial=GPIO.LOW)
    

    def a():
       run_controller(23, 94, 2)

    def b():
        run_controller(23, 180, 2)


    threading.Thread(target=a).start()
    threading.Thread(target=b).start()

    # while(1):
        
    #     run_controller(23, 94, 0)
    #     run_controller(23, 180, 0)
    #     sleep(2)

    #     break
    