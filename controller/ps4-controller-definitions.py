#Imports
from time import sleep
from roboclaw import Roboclaw
from pyPS4Controller.controller import Controller
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
# from picamera import PiCamera

#Defining PiCamera
# camera = PiCamera()

#PiGpio for servos to reduce flutter
factory = PiGPIOFactory()

#Establishing servos
servoBarLift = Servo(22, pin_factory=factory, min_pulse_width=553/1000000, max_pulse_width=2425/1000000)
servoGripper = Servo(17, pin_factory=factory, min_pulse_width=553/1000000, max_pulse_width=2425/1000000)

#address' for motors
address128 = 0x80
address129 = 0x81
address130 = 0x82


#Opening roboclaw?
roboclaw = Roboclaw("/dev/serial0", 38400)
result = roboclaw.Open()
if result == 0:
    print('Unable to open port')

 
#Event Based Coding
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    


    # Bar Lift controls
        #Bar lift Up
    def on_triangle_press(self):
        print('Bar Lift Up')
        servoBarLift.value = 0.5
        #Bar lift Down
    def on_x_press(self):
        print('Bar Lift Down')
        servoBarLift.value = -0.8

    # Gripper controls
        #Gripper Open
    def on_square_press(self):
        print('Gripper Open')
        servoGripper.value = 1
        #Gripper Close
    def on_circle_press(self):
        print('Gripper Close')
        servoGripper.value = -1

    #detach gripper and barlift
    def on_options_press(self):
        print("detach barlift and gripper")
        servoBarLift.value = None
        servoGripper.value = None



    # Linear Slide controls
        #Linear Slide Up
    def on_up_arrow_press(self):
        print('Linear Slide Up')
        roboclaw.ForwardM1(address130, 64)
        #Linear Slide Down
    def on_down_arrow_press(self):
        print('Linear Slide Down')
        roboclaw.BackwardM1(address130, 64)
    # Stop slide
    def on_up_down_arrow_release(self):
        print('Linear Slide Stop')
        roboclaw.ForwardM1(address130, 0)



    # Chassis controls
        #Move forward
    def on_R3_down(self, arg):
        print('Move forward' + str(arg))
        roboclaw.ForwardM1(address129, 20)
        roboclaw.ForwardM2(address129, 20)
        roboclaw.ForwardM1(address128, 20)
        roboclaw.ForwardM2(address128, 20)

        #Move backward
    def on_R3_up(self, arg):
        print('Move backward' + str(arg))
        # TODO
        roboclaw.BackwardM1(address129, 20)
        roboclaw.BackwardM2(address129, 20)
        roboclaw.BackwardM1(address128, 20)
        roboclaw.BackwardM2(address128, 20)
        
        #Move Left
    def on_L3_left(self, arg):
        print('Move left' + str(arg))
        # TODO
        roboclaw.BackwardM1(address129, 20)
        roboclaw.ForwardM2(address129, 20)
        roboclaw.ForwardM1(address128, 20)
        roboclaw.BackwardM2(address128, 20)
        
        #Move Right
    def on_L3_right(self, arg):
        print('Move right' + str(arg))
        # TODO
        roboclaw.ForwardM1(address129, 20)
        roboclaw.BackwardM2(address129, 20)
        roboclaw.BackwardM1(address128, 20)
        roboclaw.ForwardM2(address128, 20)

    #motor kill
        #Motor stop at y rest on R3
    def on_R3_y_at_rest(self):
        roboclaw.ForwardM1(address128, 0)
        roboclaw.ForwardM2(address128, 0)
        roboclaw.ForwardM1(address129, 0)
        roboclaw.ForwardM2(address129, 0)
        #Motor stop at x rest on R3
    def on_L3_x_at_rest(self):
        roboclaw.ForwardM1(address128, 0)
        roboclaw.ForwardM2(address128, 0)
        roboclaw.ForwardM1(address129, 0)
        roboclaw.ForwardM2(address129, 0)
    def on_share_press(self):
        roboclaw.ForwardM1(address128, 0)
        roboclaw.ForwardM2(address128, 0)
        roboclaw.ForwardM1(address129, 0)
        roboclaw.ForwardM2(address129, 0)


    # def on_playstation_button_press(self):
    #     camera.capture()

    # def on_R1_press(self):
    #     camera.start_preview()
    # def on_R1_release(self):
    #     camera.stop_preview()



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=10)    


#True holonomic code (not hardcoded)
# while still_running==True:
#     roboclaw.ForwardBackwardM1(address129, (axis1_UD_R3 - axis3_LR_L3 - axis2_LR_R3))
#     roboclaw.ForwardBackwardM2(address129, (axis1_UD_R3 - axis3_LR_L3 + axis2_LR_R3))
#     roboclaw.ForwardBackwardM1(address128, (axis1_UD_R3 + axis3_LR_L3 + axis2_LR_R3))
#     roboclaw.ForwardBackwardM2(address128, (axis1_UD_R3 + axis3_LR_L3 - axis2_LR_R3))