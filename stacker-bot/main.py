from pyPS4Controller.controller import Controller
from roboclaw import Roboclaw
from time import sleep

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    # sample ps4 event handlers
    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")

   # Event handlers for chassis control
    def on_R3_down(self, arg):
        print('R3 down: ' + str(round(arg)))
        roboclaw.ForwardM1(0x80,64)
        roboclaw.ForwardM2(0x80,64)
        roboclaw.ForwardM1(0x81,64)
        roboclaw.ForwardM2(0x81,64)

    def on_R3_up(self, arg):
        print('R3 up: ' + str(round(arg)))
        roboclaw.BackwardM1(0x80,64)
        roboclaw.BackwardM2(0x80,64)
        roboclaw.BackwardM1(0x81,64)
        roboclaw.BackwardM2(0x81,64)

    def on_R3_left(self, arg):
        print('R3 left: ' + str(round(arg)))

    def on_R3_right(self, arg):
        print('R3 right: ' + str(round(arg)))

    def on_R3_y_at_rest(self):
        print("r3 y rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)
     
    def on_R3_x_at_rest(self):
        print("r3 x rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)
   
    def on_share_press(self):
        print("share press")


if __name__ == "__main__":
    
    address = 0x80
    roboclaw = Roboclaw("/dev/serial0", 38400)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')
    print('Printing connection result - ' + str(result))
    print('Connection - ' + str(roboclaw._port.is_open))
    
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=6)