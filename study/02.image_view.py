import cv2

src = cv2.imread("../img/OpenCV_Logo.png", cv2.IMERAD_GRAYSCALE)

cv2.namedWindow("src", flags = cv2.WINDOW_FREERATIO)   #src 이름창을 생성
cv2.resizeWindow("src", 400, 200)    # src 너비 = 400 , 높이 = 400
cv2.imshow("src", 400, 200)    # src 창에 src를 출력
cv2.imshow("src", src)
cv2.waitkey(0)     # 0이면무한대기
cv2.destroyWindow("src")      # src창을 없애라

