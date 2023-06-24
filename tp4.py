import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread("aro.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar un umbral para obtener los bordes
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Aplicar la transformada de Hough para detectar círculos
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=5, maxRadius=50)

# Si se detectaron círculos, dibujarlos en la imagen original
if circles is not None:
    circles = np.round(circles[0, :]).astype(int)
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# Mostrar la imagen con los círculos detectados
cv2.imshow("Círculos detectados", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
