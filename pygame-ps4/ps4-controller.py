import pygame

# pygame.init()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()


# Get count of joysticks.
joystick_count = pygame.joystick.get_count()

print("Number of joysticks: {}".format(joystick_count))


# # For each joystick:
# for i in range(joystick_count):
#     joystick = pygame.joystick.Joystick(i)
#     joystick.init()

#     try:
#         jid = joystick.get_instance_id()
#     except AttributeError:
#         # get_instance_id() is an SDL2 method
#         jid = joystick.get_id()
#     print("Joystick {}".format(jid))

#     # Get the name from the OS for the controller/joystick.
#     name = joystick.get_name()
#     print("Joystick name: {}".format(name))

#     try:
#         guid = joystick.get_guid()
#     except AttributeError:
#         # get_guid() is an SDL2 method
#         pass
#     else:
#         print("GUID: {}".format(guid))

#     # Usually axis run in pairs, up/down for one, and left/right for
#     # the other.
#     axes = joystick.get_numaxes()
#     print("Number of axes: {}".format(axes))
    

#     for i in range(axes):
#         axis = joystick.get_axis(i)
#         print("Axis {} value: {:>6.3f}".format(i, axis))
    

#     buttons = joystick.get_numbuttons()
#     print("Number of buttons: {}".format(buttons))
    

#     for i in range(buttons):
#         button = joystick.get_button(i)
#         print("Button {:>2} value: {}".format(i, button))
    

#     hats = joystick.get_numhats()
#     print("Number of hats: {}".format(hats))
    

#     # Hat position. All or nothing for direction, not a float like
#     # get_axis(). Position is a tuple of int values (x, y).
#     for i in range(hats):
#         hat = joystick.get_hat(i)
#         print("Hat {} value: {}".format(i, str(hat)))

counter = 100
# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    if counter > 0:
        counter = counter - 1
    else:
        done = True

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
