# https://www.youtube.com/watch?v=Pbv0QES7Is8
import cv2
import numpy as np
import pyautogui
import time
# import win32gui
# import win32con
import os

# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
# DISPLAY SCREEN RESULATION, GET IT FROM OS SETTINGS
SCREEN_SIZE = (1920, 1080)

# DEFINE CODEC
fourcc = cv2.VideoWriter_fourcc(*"XVID")


# CREATE VIDEO WRITER OBJECT
# SETTING THE FILE NAME
output = cv2.VideoWriter("recordings/"+"screen-recording-"+time.strtime("%H-%M-^S %d-%m-%y")+'.mp4', fourcc, 20.0, (SCREEN_SIZE))
print("recording started, \n window minimised taskbar \n press q to exit")


#  PROCESSING THE VIDEO
while True:
    # TAKE SCREENSHORT
    img = pyautogui.screenshot()
    # CONVERT IT TO PIXELS TO A PROPER NUMPY ARRAY TO WORK WITH OPEN CV
    frame = np.array(img)
    # COVERT COLOR FROM BGR TO RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # SHOW THE FRAME
    cv2.imshow("Screen recoder", frame)
    # WRITE THE FRAME
    output.write(frame)
    if cv2.waitKey(1) == ord("q"):
        print("\r Recording finished")
        break


# MAKE SURE EVERYTHING IS CLOSED WITH EXITED
output.release()
cv2.destroyWindow()