from roboclaw import Roboclaw
from time import sleep
from pyPS4Controller.controller import Controller

if __name__ == "__main__":
    

    '''
    Addressi for the claws
    128 - back motors
    129 - front motors
    130 - slide
    '''
    address128 = 0x80
    address129 = 0x81
    address130 = 0x82

    roboclaw = Roboclaw("/dev/serial0", 38400)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
    #going forward with triangle press for M1
    def on_triangle_press(self):
        print('Linear Slide Up')
        roboclaw.ForwardM1(address130,64)

    #STOP going forward with triangle press for M1
    def on_triangle_release(self):
        print('Linear Slide Stop')
        roboclaw.ForwardM1(address130,0)

    #going forward with up arrow press for M2
    def on_x_press(self):
        print('Linear Slide Down')
        roboclaw.BackwardM1(address130,64)

    #STOP going forward with up arrow press for M2
    def on_x_release(self):
        print('Linear Slide Stop')
        roboclaw.BackwardM1(address130,0)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=6)    
