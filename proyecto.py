import numpy as np
import cv2
  
  
# define a video capture object

def cange_res(vid:cv2.VideoCapture, width, height):
    vid.set(3, width)
    vid.set(3, width)
# frames_per_second=10
# save_path='aca.mp4'
# config=
  


while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    
  
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame1', frame)
    cv2.imshow('frame1', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # elif cv2.waitKey(1) & 0xFF == ord('p'):
    #     cv2.imshow('frame', gray)
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()