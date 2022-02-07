from pyPS4Controller.controller import Controller
from roboclaw import Roboclaw
from PCA9685 import PCA9685
from time import sleep

speed = 20
Lspeed = 20
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    # sample ps4 event handlers
    def on_x_press(self):
        print("On X Press")
        for i in range(2000,1300,-10):
            pwm.setServoPulse(0,i) 
            sleep(0.02)
        pwm.setPWM(0, 0, 4096)

    def on_x_release(self):
        print("Goodbye world")
        for i in range(1300,2000,10):  
            pwm.setServoPulse(0,i)   
            sleep(0.02)

    # Event handlers for linear slide

        #Up
    def on_up_arrow_press(self):
        print("Linear slide Up")
        roboclaw.ForwardM1(0x82,Lspeed)

        #Down
    def on_down_arrow_press(self):
        print("Linear slide Down")
        roboclaw.BackwardM1(0x82,Lspeed)

        #Release
    def on_up_down_arrow_release(self):
        print("Linear slide Stop")
        roboclaw.ForwardM1(0x82,0)
        #roboclaw.BackwardM1(0x82,0)


    # Event handlers for chassis control
        #Down
    def on_L2_press(self, arg):
        print('R3 down: ' + str(round(arg)))
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

        #Up
    def on_R2_press(self, arg):
        print('R3 up: ' + str(round(arg)))
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Left
    def on_L1_press(self):
        print('R3 left: ')
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

        #Right
    def on_R1_press(self):
        print('R3 right: ')
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Rotate Left
    def on_left_arrow_press(self):
        print('R3 left: ')
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Rotate right
    def on_right_arrow_press(self):
        print('R3 right: ')
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

        #At rest y-axis on r3
    def on_L2_release(self):
        print("r3 y rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)
     
        #At rest x-axis on r3
    def on_R2_release(self):
        print("r3 x rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)

        #At rest x-axis on l3
    def on_R1_release(self):
        print("r3 x rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)
   
    def on_L1_release(self):
        print("share press")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)

    def on_left_right_arrow_release(self):
        print("share press")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)

    def on_share_press(self):
        print("share press")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)



if __name__ == "__main__":
    
    address = 0x80
    roboclaw = Roboclaw("/dev/serial0", 38400)
    result = roboclaw.Open()
    if result == 0:
        print('Unable to open port')
    print('Printing connection result - ' + str(result))
    print('Connection - ' + str(roboclaw._port.is_open))
    
    pwm = PCA9685(0x40, debug=True)
    pwm.setPWMFreq(50)
    gripper_pulse = 2000

    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=6)


#    # Event handlers for chassis control

#         #Down
#     def on_R3_down(self, arg):
#         print('R3 down: ' + str(round(arg)))
#         roboclaw.ForwardM1(0x80,speed)
#         roboclaw.ForwardM2(0x80,speed)
#         roboclaw.ForwardM1(0x81,speed)
#         roboclaw.ForwardM2(0x81,speed)

#         #Up
#     def on_R3_up(self, arg):
#         print('R3 up: ' + str(round(arg)))
#         roboclaw.BackwardM1(0x80,speed)
#         roboclaw.BackwardM2(0x80,speed)
#         roboclaw.BackwardM1(0x81,speed)
#         roboclaw.BackwardM2(0x81,speed)

#         #Left
#     def on_R3_left(self, arg):
#         print('R3 left: ' + str(round(arg)))
#         roboclaw.ForwardM1(0x80,speed)
#         roboclaw.BackwardM2(0x80,speed)
#         roboclaw.BackwardM1(0x81,speed)
#         roboclaw.ForwardM2(0x81,speed)

#         #Right
#     def on_R3_right(self, arg):
#         print('R3 right: ' + str(round(arg)))
#         roboclaw.BackwardM1(0x80,speed)
#         roboclaw.ForwardM2(0x80,speed)
#         roboclaw.ForwardM1(0x81,speed)
#         roboclaw.BackwardM2(0x81,speed)

#         #Rotate Left
#     def on_L3_left(self, arg):
#         print('R3 left: ' + str(round(arg)))
#         roboclaw.ForwardM1(0x80,speed)
#         roboclaw.BackwardM2(0x80,speed)
#         roboclaw.ForwardM1(0x81,speed)
#         roboclaw.BackwardM2(0x81,speed)

#         #Rotate right
#     def on_L3_right(self, arg):
#         print('R3 right: ' + str(round(arg)))
#         roboclaw.BackwardM1(0x80,speed)
#         roboclaw.ForwardM2(0x80,speed)
#         roboclaw.BackwardM1(0x81,speed)
#         roboclaw.ForwardM2(0x81,speed)

#         #At rest y-axis on r3
#     def on_R3_y_at_rest(self):
#         print("r3 y rest")
#         roboclaw.ForwardM1(0x80,0)
#         roboclaw.ForwardM2(0x80,0)
#         roboclaw.ForwardM1(0x81,0)
#         roboclaw.ForwardM2(0x81,0)
     
#         #At rest x-axis on r3
#     def on_R3_x_at_rest(self):
#         print("r3 x rest")
#         roboclaw.ForwardM1(0x80,0)
#         roboclaw.ForwardM2(0x80,0)
#         roboclaw.ForwardM1(0x81,0)
#         roboclaw.ForwardM2(0x81,0)

#         #At rest x-axis on l3
#     def on_L3_x_at_rest(self):
#         print("r3 x rest")
#         roboclaw.ForwardM1(0x80,0)
#         roboclaw.ForwardM2(0x80,0)
#         roboclaw.ForwardM1(0x81,0)
#         roboclaw.ForwardM2(0x81,0)
   
#     def on_share_press(self):
#         print("share press")
#         roboclaw.ForwardM1(0x80,0)
#         roboclaw.ForwardM2(0x80,0)
#         roboclaw.ForwardM1(0x81,0)
#         roboclaw.ForwardM2(0x81,0)

