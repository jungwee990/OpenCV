#Hue 공간 색상검출
import cv2

src = cv2.imread("../img/tomato.jpg")
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(hsv)
#h_red = cv2.inRange(h,0,5)
h_red = cv2.inRange(h,16,40)

dst = cv2.bitwise_and(hsv, hsv, mask = h_red)
dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()