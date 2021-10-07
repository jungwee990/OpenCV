import cv2

src = cv2.imread("../img/ferris-wheel.jpg")
dst = src.copy()

for i in range(3):
    dst = cv2.pyrDown(dst)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitkey(0)
cv2.destroyAllWindows()
