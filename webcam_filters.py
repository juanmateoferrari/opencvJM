from configparser import Interpolation
import time
import cv2
import numpy as np

cap = (cv2.VideoCapture(0 + cv2.CAP_DSHOW))

WIDTH, HEIGHT = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

global cell_width, cell_heigth
cell_width, cell_heigth = 12, 12
global new_width, new_heigth
new_width, new_heigth = int(WIDTH / cell_width) , int(HEIGHT / cell_heigth)

global flag
flag=True




def effect(image, flag):
    global black_window, small_image

    black_window=np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    small_image = cv2.resize(image, (new_width, new_heigth), interpolation=cv2.INTER_NEAREST)

    # change_pixel_size()
    
    for i in range(new_heigth):
        for j in range(new_width):
            color = small_image[i,j]
            B=int(color[0])
            G=int(color[1])
            R=int(color[2])

            coord=(j * cell_width + cell_width, i * cell_heigth)
            if flag:
                
                cv2.circle(black_window, coord, 10, (B, G, R), -1)

            else:
                cv2.line(black_window, coord, (coord[0] + 10, coord[1]), (0,G,0) ,1)
                cv2.line(black_window,(coord[0] + 6, coord[1]-6), (coord[0] + 6, coord[1]+6), (0,0,R) ,1)


while True:

    _, frame = cap.read()

    # cv2.imshow('result', frame)

    effect(frame, flag)

    # cv2.blur(frame, 5)

    # cv2.imshow('effect', small_image)

    cv2.imshow('effect', black_window)

    # if cv2.waitKey(1) & 0xFF =='c':
    #     flag= not flag

    if cv2.waitKey(1) & 0xFF =='c':
        flag= not flag
        # 
    # if cv2.waitKey(1) & 0xFF ==27:
    #     break

    time.sleep(0.4)

cv2.destroyAllWindows()
