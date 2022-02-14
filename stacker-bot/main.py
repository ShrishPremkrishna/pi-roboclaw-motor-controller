from pyPS4Controller.controller import Controller
from roboclaw import Roboclaw
from PCA9685 import PCA9685
from time import sleep

speed = 20
Lspeed = 35




class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.gripper_pulse = 2000
        self.gripper_channel = 0
        self.gripper_max = 2000
        self.gripper_min = 1200

        self.barlift_pulse = 600
        self.barlift_channel = 2
        self.barlift_max = 2200
        self.barlift_min = 600

        self.cam_pulse = 1400
        self.cam_channel = 4
        self.cam_max = 2300
        self.cam_min = 1400

    # Gripper controls
    # close
    def on_square_press(self):
        print("On X Press")
        if (self.gripper_pulse > self.gripper_min) :
            self.gripper_pulse = self.gripper_pulse - 100
            pwm.setServoPulse(self.gripper_channel, self.gripper_pulse) 
            sleep(0.02)
        
    # def on_square_release(self):
    #     pwm.setPWM(self.gripper_channel, 0, 4096)

    def on_circle_press(self):
        print("On Triangle Press")
        if (self.gripper_pulse < self.gripper_max) :
            self.gripper_pulse = self.gripper_pulse + 200
            pwm.setServoPulse(self.gripper_channel, self.gripper_pulse) 
            sleep(0.02)
        
    # def on_circle_release(self):
    #     pwm.setPWM(self.gripper_channel, 0, 4096)

    def on_options_press(self):
        pwm.setPWM(self.gripper_channel, 0, 4096)

    # Bar Lift controls
    def on_triangle_press(self):
        print("On Traingle Press - lift barlift")
        print("Barlift pulse at - " + str(self.barlift_pulse))
        if (self.barlift_pulse < self.barlift_max) :
            for i in range(self.barlift_pulse, self.barlift_pulse + 200, 10):  
                pwm.setServoPulse(self.barlift_channel, i)   
                sleep(0.02) 
            print("Barlift pulse being set at - " + str(self.barlift_pulse))
            self.barlift_pulse = self.barlift_pulse + 200 

    def on_x_press(self):
        print("On X Press - lower barlift")
        print("Barlift pulse at - " + str(self.barlift_pulse))
        if (self.barlift_pulse > self.barlift_min) :
            print("Barlift pulse being set at - " + str(self.barlift_pulse))
            for i in range(self.barlift_pulse, self.barlift_pulse - 200, -10):  
                pwm.setServoPulse(self.barlift_channel, i)   
                sleep(0.02) 
            self.barlift_pulse = self.barlift_pulse - 200


        if (self.barlift_pulse <= self.barlift_min + 100):
            pwm.setPWM(self.barlift_channel, 0, 4096)

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

    # Event handlers for Camera

    def on_R3_press(self):
        print("R3 Press")
        print("Cam pulse at - " + str(self.cam_pulse))
        if (self.cam_pulse < self.cam_max) :
            for i in range(self.cam_pulse, self.cam_pulse + 100, 10):  
                pwm.setServoPulse(self.cam_channel, i)   
                sleep(0.02) 
            print("Cam pulse being set at - " + str(self.cam_pulse))
            self.cam_pulse = self.cam_pulse + 100 

    def on_L3_press(self):
        print("L3 Press")
        print("Cam pulse at - " + str(self.cam_pulse))
        if (self.cam_pulse > self.cam_min) :
            print("Cam pulse being set at - " + str(self.cam_pulse))
            for i in range(self.cam_pulse, self.cam_pulse - 100, -10):  
                pwm.setServoPulse(self.cam_channel, i)   
                sleep(0.02) 
            self.cam_pulse = self.cam_pulse - 100


        if (self.cam_pulse <= self.cam_min + 100):
            pwm.setPWM(self.cam_channel, 0, 4096)

    # Event handlers for chassis control
        #Down
    def on_L2_press(self, arg):
        print('L2 down: ' + str(round(arg)))
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

        #Up
    def on_R2_press(self, arg):
        print('R2 up: ' + str(round(arg)))
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Left
    def on_L1_press(self):
        print('L1 left: ')
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Right
    def on_R1_press(self):
        print('R1 right: ')
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

        #Rotate Left
    def on_left_arrow_press(self):
        print('Left Arrow left: ')
        roboclaw.ForwardM1(0x80,speed)
        roboclaw.BackwardM2(0x80,speed)
        roboclaw.ForwardM1(0x81,speed)
        roboclaw.BackwardM2(0x81,speed)

        #Rotate right
    def on_right_arrow_press(self):
        print('Right Arrow right: ')
        roboclaw.BackwardM1(0x80,speed)
        roboclaw.ForwardM2(0x80,speed)
        roboclaw.BackwardM1(0x81,speed)
        roboclaw.ForwardM2(0x81,speed)

    #RELEASES (stops motors)
    def on_L2_release(self):
        print("L2 y rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)
     
    def on_R2_release(self):
        print("r2 x rest")
        roboclaw.ForwardM1(0x80,0)
        roboclaw.ForwardM2(0x80,0)
        roboclaw.ForwardM1(0x81,0)
        roboclaw.ForwardM2(0x81,0)

    def on_R1_release(self):
        print("r1 x rest")
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
    
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    pwm.setPWM(0, 0, 4096)
    pwm.setPWM(2, 0, 4096)
    pwm.setPWM(4, 0, 4096)

    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen(timeout=6)



    # camera = cv2.VideoCapture(0)
    # cv2.namedWindow("test")

    # img_counter = 0

    # while True:
    #     ret, frame = camera.read()
    #     if not ret:
    #         print("failed to grab frame")
    #         break
    #     cv2.imshow("test", frame)

        # if k%256 == 27:
        #     # ESC pressed
        #     print("Escape hit, closing...")
        #     break
        # elif k%256 == 32:
        #     # SPACE pressed
        #     img_name = "opencv_frame_{}.png".format(img_counter)
        #     cv2.imwrite(img_name, frame)
        #     print("{} written!".format(img_name))
        #     img_counter += 1


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

