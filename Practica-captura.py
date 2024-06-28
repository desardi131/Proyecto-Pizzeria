import cv2

cap = cv2.VideoCapture(0) # funcion para capturar

while True:
    ret, frame = cap.read() 
    if not ret: # Si la camara no graba rada, el script se para
        break

    cv2.imshow('Captura de imagen', frame) # muestra la ventana que graba la camara

    if cv2.waitKey(1) & 0xFF == ord('s'): # Si presionamos la tecla 's' crea una captura y se cierra el programa
        cv2.imwrite('captura.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()