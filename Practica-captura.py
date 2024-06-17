import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Captura de imagen', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('captura.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()