import numpy as np
import cv2

#img = np.zeros((100,100,3))
img = cv2.imread("test.png")

img[:,:,0] = 218
img[:,:,1] = 219
img[:,:,2] = 172

cv2.imshow("test",img)
cv2.waitKey(0)
cv2.imshow("test.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
