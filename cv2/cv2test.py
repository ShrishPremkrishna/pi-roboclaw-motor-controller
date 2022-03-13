import cv2
import numpy as np

camera = cv2.VideoCapture(0)

# while True:
#     _, frame = camera.read()
#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# camera.release()
# cv2.destroyAllWindows()

_, frame = camera.read()
cv2.imwrite('opencv'+str(i)+'.png', image)
cv2.imwrite('image', frame)
camera.release()
