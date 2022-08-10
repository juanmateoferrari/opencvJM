import cv2
import numpy as np


class VentanaVideo:
    
    def __init__(self, puerto, alto=600, ancho=800, alto_pixel=12, ancho_pixel=12):
        self.captura=cv2.VideoCapture(puerto)
        self.puerto=puerto
        self.ancho=ancho
        self.alto=alto

        
        self.ancho_pixel=ancho_pixel
        self.alto_pixel=alto_pixel

        

        self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, self.ancho)
        self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, self.alto)

    # def mostrar_en_pantalla(self):
    def mostrar_marco(self):
        self.ret, mi_ventana.frame = self.captura.read()
        cv2.imshow('frame1', mi_ventana.frame)
    #     while True:
    #         self.ret, self.frame = self.captura.read()
    #         self.blanco_y_negro()
    #         cv2.imshow('frame1', self.frame)
            
            
    #         if self.apreta_tecla('q'):
    #             break
    #     # self.captura.release()
    #     cv2.destroyAllWindows()
    def nuevo_marco(self):
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def lineas_rojas_y_verdes(self,a=12,b=12):
        cell_width, cell_heigth = a, b
        new_width, new_heigth = int(self.ancho / cell_width) , int(self.alto / cell_heigth)
        black_window=np.zeros((self.ancho, cell_width, 3), np.uint8)
        small_image = cv2.resize(self.frame, (new_width, new_heigth), interpolation=cv2.INTER_NEAREST)

        for i in range(new_heigth):
            for j in range(new_width):
                color = small_image[i,j]
                B=int(color[0])
                G=int(color[1])
                R=int(color[2])

                coord=(j * cell_width + cell_width, i * cell_heigth)
                cv2.line(black_window, coord, (coord[0] + 10, coord[1]), (0,G,0) ,1)
                cv2.line(black_window,(coord[0] + 6, coord[1]-6), (coord[0] + 6, coord[1]+6), (0,0,R) ,1)

        self.frame=black_window

    def blanco_y_negro(self):
        self.frame=cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

    def apreta_tecla(self, tecla):
        return cv2.waitKey(1) & 0xFF == ord(tecla)



mi_ventana=VentanaVideo(0)
    
while True:
    mi_ventana.ret, mi_ventana.frame = mi_ventana.captura.read()
    mi_ventana.lineas_rojas_y_verdes()
    mi_ventana.mostrar_marco()

    
    # gray= #mi_ventana.nuevo_marco()
    # VentanaVideo.mostrar_marco(VentanaVideo.nuevo_marco())
    
    
    
    if mi_ventana.apreta_tecla('q'):
        break
# self.captura.release()
cv2.destroyAllWindows()
