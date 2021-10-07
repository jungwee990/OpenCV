import cv2

src = cv2.imread("../img/swan.jpg",cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)
# color 이미지를 바이너리로 하면 각 rgb채널별로 바이너리 한 후 합쳐진 것이다.
# 그래서 컬러이미지는 이진화하지 않는다.
# 컬러 -> 그레이 -> 이진화
cv2.namedWindow("binary")
cv2.resize(binary, (300, 300))
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
