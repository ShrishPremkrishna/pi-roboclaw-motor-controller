from time import sleep
from roboclaw import Roboclaw
from pyPS4Controller.controller import Controller
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servoBarLift = Servo(17, pin_factory=factory)
servoGripper = Servo(22, pin_factory=factory)
address128 = 0x80
address129 = 0x81
address130 = 0x82

# mecanum logic
axis1_UD_R3 = 0
axis2_LR_R3 = 0
axis3_LR_L3 = 0

roboclaw = Roboclaw("/dev/serial0", 38400)
result = roboclaw.Open()
if result == 0:
    print('Unable to open port')

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    # Bar Lift controls
    def on_triangle_press(self):
        print('Bar Lift Up')
        servoBarLift.value = 0.8

    def on_x_press(self):
        print('Bar Lift Down')
        servoBarLift.min()

    # Gripper controls
    def on_square_press(self):
        print('Gripper Open')
        servoGripper.value = 0.5

    def on_circle_press(self):
        print('Gripper Close')
        servoGripper.value = -0.5

    def on_options_press(self):
        print("detach barlift and gripper")
        servoBarLift.value = None
        servoGripper.value = None

    # Linear Slide controls
    def on_up_arrow_press(self):
        print('Linear Slide Up')
        roboclaw.ForwardM1(address130, 64)

    def on_down_arrow_press(self):
        print('Linear Slide Down')
        roboclaw.BackwardM1(address130, 64)

    def on_up_down_arrow_release(self):
        print('Linear Slide Stop')
        roboclaw.ForwardM1(address130, 0)

    # Chassis controls
    def on_R3_up(self, arg):
        print('Move forward' + str(arg))
        # TODO
        roboclaw.BackwardM1(address128, 20)
        roboclaw.BackwardM2(address128, 20)
        roboclaw.BackwardM1(address129, 20)
        roboclaw.BackwardM2(address129, 20)

    def on_R3_down(self, arg):
        print('Move backward' + str(arg))
        # TODO
        roboclaw.ForwardM1(address128, 20)
        roboclaw.ForwardM2(address128, 20)
        roboclaw.ForwardM1(address129, 20)
        roboclaw.ForwardM2(address129, 20)

    def on_R3_left(self, arg):
        print('Move left' + str(arg))
        # TODO
        roboclaw.ForwardM1(address128, 20)
        roboclaw.ForwardM2(address128, 20)
        roboclaw.ForwardM1(address129, 20)
        roboclaw.ForwardM2(address129, 20)

    def on_R3_right(self, arg):
        print('Move right' + str(arg))
        # TODO
        roboclaw.ForwardM1(address128, 20)
        roboclaw.ForwardM2(address128, 5)
        roboclaw.ForwardM1(address129, 20)
        roboclaw.ForwardM2(address129, 5)

    #motor kill
    def on_R3_y_at_rest(self):
        roboclaw.ForwardM1(address128, 0)
        roboclaw.ForwardM2(address128, 0)
        roboclaw.ForwardM1(address129, 0)
        roboclaw.ForwardM2(address129, 0)

    def on_R3_x_at_rest(self):
        roboclaw.ForwardM1(address128, 0)
        roboclaw.ForwardM2(address128, 0)
        roboclaw.ForwardM1(address129, 0)
        roboclaw.ForwardM2(address129, 0)




controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=10)    
