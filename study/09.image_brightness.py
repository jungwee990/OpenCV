import numpy as np
import cv2

src = cv2.imread('../img/psycho_But_Okay.jpg',cv2.IMREAD_GRAYSCALE)

val = 100
array = np.full(src.shape, (val,val,val), dtype = np.uint8)
add_dst = cv2.add(src,100)
sub_dst = cv2.subtract(src,100)

cv2.imshow('src', src)
cv2.imshow('add_dst', add_dst)
cv2.imshow('sub_dst', sub_dst)

cv2.waitKey()
cv2.destroyALLWindows()
