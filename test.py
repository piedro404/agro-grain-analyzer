import cv2
import numpy as np

img = cv2.imread('imagens/20251115_152402.jpg')
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()