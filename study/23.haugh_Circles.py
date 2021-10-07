import cv2

src = cv2.imread("../img/colorball.png")
#cv2.imshow("src",src);cv2.waitkey(0);cv2.destroyAllWindows("src")
dst = src.copy()

image= cv2.cv2color(src, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray",image);cv2.waitkey(0);cv2.destroyAllWindows("gray")

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3), (-1,-1))
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100, param1= 100, param2 = 35, minRadius=80, maxRadius=120)
# dilate 주변부 영역을 다듬어 준다.
# morpolygy 연산 - 모양을 정리해줌

for i in circles[0]:
    cv2.circle(dst, (i[0],i[1],i[2],(255, 255,255),5))

cv2.imshow("dst", dst)
cv2.waitkey(0)
cv2.destroyAllWindows()